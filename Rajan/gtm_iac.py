'''
This file defines the build of the O8 shared services.
This will be synthed to create a json template which will then be deployed to AWS.
This file is IaC
'''

from aws_cdk import (
    Stack, Tags,
    aws_ec2 as ec2,
    aws_ram as ram,
    aws_logs as logs,
    aws_iam as iam,
    aws_cloudwatch as cloudwatch,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_cloudwatch_actions as cwactions
)

import aws_cdk as cdk
import aws_cdk.aws_networkmanager as networkmanager

from constructs import Construct


class shared_services_transit_gateway_stack(Stack):
    '''
    This class defines all the code required for the IaC
    '''

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Name Tag variables for each construct
        self.tag_name_ss_tgw = "Shared-Services-Transit-Gateway"
        self.tag_name_ss_ram_share = "Shared-Services-Resource-Share-TGW"
        self.tag_name_ss_global_network = "Shared-Services-Global-Network"
        self.tag_name_ss_tgw_registration = "Shared-Services-TGW-Registration"
        self.tag_name_ss_vpn_cloudwatch_group = "Shared-Services-VPN-CloudWatch-2"
        self.tag_name_ss_vpn_cloudwatch_iam_role = "Shared-Services-VPN-Cloudwatch-IAM-Role"

        # Id variables for each construct
        # If you change the ID, deploy will create a new construct and delete the exisiting one
        # To just change the name then change name_tag_XXX variable, not id_XXX variable
        self.id_ss_ram_share = "Shared-Services-Resource-Share-TGW"
        self.id_ss_tgw = "Shared-Services-Transit-Gateway"
        self.id_ss_global_network = "Shared-Services-Global-Network"
        self.id_ss_tgw_registration = "Shared-Services-TGW-Registration"
        self.id_ss_customer_gw = "Shared-Services-VPN-Gateway"
        self.id_ss_vpn_connection = "Shared-Services-VPN-Connection"
        self.id_ss_vpn_cloudwatch_group = "Shared-Services-VPN-CloudWatch-Group-2"
        self.id_ss_vpn_cloudwatch_iam_role = "Shared-Services-VPN-Cloudwatch-IAM-Role"
        self.id_ss_tunnel1_metric = "Shared-Services-Tunnel1-Metric"
        self.id_ss_tunnel2_metric = "Shared-Services-Tunnel2-Metric"
        self.id_ss_tunnel1_alarm = "Shared-Services-Tunnel1-Alarm"
        self.id_ss_tunnel2_alarm = "Shared-Services-Tunnel2-Alarm"

        # Build variables to define organisation ID or CIDRs
        self.id_ss_organisation = "arn:aws:organizations::820673055100:organization/o-cur60mbsvz"

        # create a Transit Gateway
        cdk_tgw = ec2.CfnTransitGateway(
            self,
            self.id_ss_tgw,
            tags=[cdk.CfnTag(key="Name", value=self.tag_name_ss_tgw)],
            dns_support="enable",
            vpn_ecmp_support="enable",
            default_route_table_association="disable",
            default_route_table_propagation="disable",
            auto_accept_shared_attachments="enable",
            multicast_support="disable",
        )

        # create a resource share in AWS RAM in shared services
        ss_resource_share = ram.CfnResourceShare(
            self,
            name=self.tag_name_ss_ram_share,
            id=self.id_ss_ram_share,
            allow_external_principals=False,
            principals=[self.id_ss_organisation],
            resource_arns=[cdk_tgw.attr_transit_gateway_arn],
        )

        # update the name of the TGW Resource Share
        Tags.of(ss_resource_share).add("Name", self.tag_name_ss_ram_share)

        # create a new aws network manager using the global network
        ss_global_network = networkmanager.CfnGlobalNetwork(
            self,
            self.id_ss_global_network,
            description=self.tag_name_ss_global_network,
            state="AVAILABLE",
            tags=[cdk.CfnTag(key="Name", value=self.tag_name_ss_global_network)]
        )

        # register the transit gateway to the global network
        cdk_tgw_registration = networkmanager.CfnTransitGatewayRegistration(
            self,
            self.id_ss_tgw_registration,
            global_network_id=ss_global_network.attr_id,
            transit_gateway_arn=cdk_tgw.attr_transit_gateway_arn
        )

        # create a customer gateway
        ss_customer_gw = ec2.CfnCustomerGateway(
            self,
            self.id_ss_customer_gw,
            ip_address="4.234.146.188",
            bgp_asn=65000,
            type="ipsec.1"
        )

        # create a cloudwatch log group
        vpn_cloudwatch_log_group = logs.CfnLogGroup(
            self,
            self.id_ss_vpn_cloudwatch_group,
            log_group_name=self.tag_name_ss_vpn_cloudwatch_group,
            retention_in_days=90,
            tags=[cdk.CfnTag(key="Name", value=self.tag_name_ss_vpn_cloudwatch_group)]
        )

        # create an IAM role for the VPN to write to cloudwatch logs
        vpn_cloudwatch_role = iam.Role(
            self,
            self.id_ss_vpn_cloudwatch_iam_role,
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            role_name=self.tag_name_ss_vpn_cloudwatch_iam_role
        )

        # add permissions to the IAM role
        vpn_cloudwatch_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                    "logs:DescribeLogGroups",
                    "logs:DescribeLogStreams"
                ],
                resources=[vpn_cloudwatch_log_group.attr_arn]
            )
        )

        # create a VPN connection for the gateway
        ss_vpn_connection = ec2.CfnVPNConnection(
            self,
            self.id_ss_vpn_connection,
            static_routes_only=True,
            customer_gateway_id=ss_customer_gw.attr_customer_gateway_id,
            type="ipsec.1",
            transit_gateway_id=cdk_tgw.attr_id,
            local_ipv4_network_cidr="172.29.32.0/20",
            remote_ipv4_network_cidr="10.0.0.0/13",
        )

        # add the tunnel log options
        ss_vpn_connection.add_property_override("VpnTunnelOptionsSpecifications", [
            {
                "Phase1EncryptionAlgorithms": [{"Value": "AES256"}, {"Value": "AES256-GCM-16"}],
                "Phase2EncryptionAlgorithms": [{"Value": "AES256"}, {"Value": "AES256-GCM-16"}],
                "Phase1IntegrityAlgorithms": [{"Value": "SHA2-256"}, {"Value": "SHA2-384"}, {"Value": "SHA2-512"}],
                "Phase2IntegrityAlgorithms": [{"Value": "SHA2-256"}, {"Value": "SHA2-384"}, {"Value": "SHA2-512"}],
                "IKEVersions": [{"Value": "ikev2"}],
                "LogOptions": {
                    "CloudwatchLogOptions": {
                        "LogEnabled": True,
                        "LogGroupArn": vpn_cloudwatch_log_group.attr_arn}
                }},
            {
                "Phase1EncryptionAlgorithms": [{"Value": "AES256"}, {"Value": "AES256-GCM-16"}],
                "Phase2EncryptionAlgorithms": [{"Value": "AES256"}, {"Value": "AES256-GCM-16"}],
                "Phase1IntegrityAlgorithms": [{"Value": "SHA2-256"}, {"Value": "SHA2-384"}, {"Value": "SHA2-512"}],
                "Phase2IntegrityAlgorithms": [{"Value": "SHA2-256"}, {"Value": "SHA2-384"}, {"Value": "SHA2-512"}],
                "IKEVersions": [{"Value": "ikev2"}],
                "LogOptions": {
                    "CloudwatchLogOptions": {
                        "LogEnabled": True,
                        "LogGroupArn": vpn_cloudwatch_log_group.attr_arn}
                }}])

        # create an sns topic for the alarms
        vpn_alarm_sns_topic = sns.Topic(
            self,
            "VPNAlarmSNSTopic",
            topic_name="VPNAlarmSNSTopic"
        )

        # add an email address to the topic
        vpn_alarm_sns_topic.add_subscription(subscriptions.EmailSubscription("awsmanagement@origin8tive.com"))

        # create a cloudwatch alarm for both tunnels
        # tunnel 1 alarm
        tunnel1_down_alarm = cloudwatch.Alarm(
            self,
            self.id_ss_tunnel1_alarm,
            alarm_name="Tunnel1Down",
            metric=cloudwatch.Metric(
                metric_name="TunnelState",
                namespace="AWS/VPN",
                dimensions_map={
                    "VpnId": ss_vpn_connection.attr_vpn_connection_id,
                    "TunnelIpAddress": "18.171.64.103"
                },
                statistic="Sum",
                period=cdk.Duration.minutes(5)
            ),
            threshold=1,
            evaluation_periods=3,
            comparison_operator=cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
            datapoints_to_alarm=3,
            alarm_description="Tunnel 1 has been down for 15 mins"
        )

        # tunnel 2 alarm
        tunnel2_down_alarm = cloudwatch.Alarm(
            self,
            self.id_ss_tunnel2_alarm,
            alarm_name="Tunnel2Down",
            metric=cloudwatch.Metric(
                metric_name="TunnelState",
                namespace="AWS/VPN",
                dimensions_map={
                    "VpnId": ss_vpn_connection.attr_vpn_connection_id,
                    "TunnelIpAddress": "35.179.199.19"
                },
                statistic="Sum",
                period=cdk.Duration.minutes(5)
            ),
            threshold=1,
            evaluation_periods=3,
            comparison_operator=cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
            datapoints_to_alarm=3,
            alarm_description="Tunnel 2 has been down for 15 mins"
        )

        # publish the tunnel 1 alarm to the SNS topic
        tunnel1_down_alarm.add_alarm_action(cwactions.SnsAction(vpn_alarm_sns_topic))

        # publish the tunnel 2 alarm to the SNS topic
        tunnel2_down_alarm.add_alarm_action(cwactions.SnsAction(vpn_alarm_sns_topic))

        # dependency for the cloud watch log group to be created before the vpn connection
        ss_vpn_connection.add_dependency(vpn_cloudwatch_log_group)

        # dependencies
        # A dependancy to ensure the resource share is not created until after the transit gateway
        ss_resource_share.add_dependency(cdk_tgw)

        # A dependancy to ensure the global network is not created until after the transit gateway
        ss_global_network.add_dependency(cdk_tgw)

        # A dependancy to ensure the tgw registration is not completed until after the global network
        cdk_tgw_registration.add_dependency(ss_global_network)

        # A dependancy to ensure the tgw registration is not completed until after the tgw created
        cdk_tgw_registration.add_dependency(cdk_tgw)

        # Outputs that may be required for future stacks
        # create an output for the tgw id
        cdk.CfnOutput(self,
                      "TGWIDExport",
                      value=cdk_tgw.attr_id,
                      export_name="TGWIDExport")
        # create an output for the tgw arn
        cdk.CfnOutput(self,
                      "TGWARNExport",
                      value=cdk_tgw.attr_transit_gateway_arn,
                      export_name="TGWARNExport")
        # create an output for the resource share id
        cdk.CfnOutput(self,
                      "RSIDExport",
                      value=ss_resource_share.logical_id,
                      export_name="RSIDExport")
        # create an output for the resource share arn
        cdk.CfnOutput(self,
                      "RSARNExport",
                      value=ss_resource_share.attr_arn,
                      export_name="RSARNExport")

        # output the log group arn
        cdk.CfnOutput(self,
                      "VPNCloudWatchLogGroupARNExport",
                      value=vpn_cloudwatch_log_group.attr_arn,
                      export_name="VPNCloudWatchLogGroupARNExport")

        # output the VPN ID
        cdk.CfnOutput(self,
                      "VPNIDExport",
                      value=ss_vpn_connection.attr_vpn_connection_id,
                      export_name="VPNIDExport")
