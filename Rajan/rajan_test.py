"""
Unit tests for validating the configuration of AWS Transit Gateway and Resource Share
using pytest. This module includes tests to ensure that the expected resources and
properties are defined correctly in the provided JSON and Python IaC code.
"""
import json
import re # to use re library for searching pattern in text
import pytest

# pylint ignore specific error codes
# pylint: disable=W0621, C0301, C0303

# Utility function to format test results
def format_test_result(test_name, expected, actual, result):
    """
    Format test results for clear output.

    Args:
        test_name (str): Name of the test case.
        expected: The expected result.
        actual: The actual result.
        result (bool): Whether the test passed.

    Returns:
        str: A formatted string with test results.
    """

    output = "Test Pass" if result else f"Test Fail - Expected {expected} but got {actual}"
    return f"\n{test_name}:\nExpected Result: {expected}\nActual Result: {actual}\nOutput: {output}"

# Utility function to extract values using regex
def extract_value(content, pattern):
    """
    Extract a value from the Python IaC code using regex.

    Args:
        content (str): Python IaC code as a string.
        pattern (str): Regex pattern to search for.

    Returns:
        str or None: The extracted value or None if no match.
    """

    match = re.search(pattern, content)
    return match.group(1) if match else None

# Utility function to validate tag names
def validate_tag_name(resource, expected_tag_name):
    """
    Validate the tag name of a given resource.

    Args:
        resource (dict): The resource object containing the tag information.
        expected_tag_name (str): The expected value of the tag name.

    Returns:
        bool: True if the tag name matches the expected value, False otherwise.
        str or None: The actual tag name found in the resource or None if not found.
    """
    if "Properties" not in resource:
        return False, None

    actual_tag_name = None
    try:
        # Check if the resource has a 'Tags' key
        if "Tags" in resource["Properties"]:
            actual_tag_name = next(
                (tag["Value"] for tag in resource["Properties"]["Tags"] if tag["Key"] == "Name"),
                None,
            )
        else:
            actual_tag_name = resource["Properties"].get("Name", None)

        return actual_tag_name == expected_tag_name, actual_tag_name
    except (KeyError, TypeError, StopIteration,) as e:
        print(f"Error While validating tag name: {e}")
        return False, None


# Fixture to load JSON data from the template
@pytest.fixture(scope="module")
def json_data():
    """
    Fixture to load JSON data from the provided template file.

    Returns:
        dict: Parsed JSON data.
    """
    json_file_path = "/home/ubuntu/shared-services-transit-gateway-stack/shared-services-transit-gateway-stack.template.json"
    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to loading JSON file: {e}")
        return ""
    except IOError as e:
        pytest.fail(f"Failed to read JSON file due to I/O error: {e}")
        return ""


# Fixture to load Python IaC code
@pytest.fixture(scope="module")
def python_code():
    """
    Fixture to load the Python IaC code from the specified file.

    Returns:
        str: Contents of the Python IaC code.
    """
    python_file_path = "/home/ubuntu/shared-services-transit-gateway-stack/shared_services_transit_gateway_stack/shared_services_transit_gateway_stack.py"
    try:
        with open(python_file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        pytest.fail(f"Python file not found: {python_file_path}")
        return ""
    except IOError as e:
        pytest.fail(f"Failed to read Python file: {e}")
        return ""


# Utility function to extract expected values from Python code
def extract_expected_values(python_code):
    """
    Extract expected values from the Python IaC code.

    Args:
        python_code (str): Contents of the Python IaC code.

    Returns:
        dict: Dictionary of expected values extracted from the Python code.
    """
    return {
        "transit_gateway_quantity": len(re.findall(r'ec2\.CfnTransitGateway', python_code)),
        "transit_gateway_tag_name": extract_value(python_code, r'self\.tag_name_ss_tgw\s*=\s*"([^"]+)"'),
        "transit_gateway_tag_id": extract_value(python_code, r'self\.id_ss_tgw\s*=\s*"([^"]+)"').replace("-", ""),
        "resource_share_quantity": len(re.findall(r'ram\.CfnResourceShare', python_code)),
        "resource_share_tag_name": extract_value(python_code, r'self\.tag_name_ss_ram_share\s*=\s*"([^"]+)"'),
        "resource_share_tag_id": extract_value(python_code, r'self\.id_ss_ram_share\s*=\s*"([^"]+)"').replace("-", ""),
        "principal_arn": extract_value(python_code, r'self\.id_ss_organisation\s*=\s*"([^"]+)"'),
        "global_network_quantity": len(re.findall(r'ec2\.CfnTransitGateway', python_code)),
        "global_network_tag_name": extract_value(python_code, r'self\.tag_name_ss_global_network\s*=\s*"([^"]+)"'),
        "global_network_tag_id": extract_value(python_code, r'self\.id_ss_global_network\s*=\s*"([^"]+)"').replace("-", ""),
        "global_network_description": extract_value(python_code, r'self\.tag_name_ss_global_network\s*=\s*"([^"]+)"'),
        "tgw_registration_quantity": len(re.findall(r'networkmanager\.CfnTransitGatewayRegistration', python_code)),
        "tgw_registration_tag_id": extract_value(python_code, r'self\.id_ss_tgw_registration\s*=\s*"([^"]+)"').replace("-", ""),
        "vpn_gateway_quantity": len(re.findall(r'ec2\.CfnCustomerGateway', python_code)),
        "vpn_gateway_tag_id": extract_value(python_code, r'self\.id_ss_customer_gw\s*=\s*"([^"]+)"').replace("-", ""),
        "vpn_gateway_ip_address": extract_value(python_code, r'ip_address\s*=\s*"([^"]+)"'),
        "vpn_gateway_bgp_asn": int(extract_value(python_code, r'bgp_asn\s*=\s*(\d+)')),
        "vpn_gateway_type": extract_value(python_code, r'type\s*=\s*"([^"]+)"'),
        "cloudwatch_group2_quantity": len(re.findall(r'logs\.CfnLogGroup', python_code)),
        "cloudwatch_group2_tag_name": extract_value(python_code, r'self\.tag_name_ss_vpn_cloudwatch_group\s*=\s*"([^"]+)"'),
        "cloudwatch_group2_tag_id": extract_value(python_code, r'self\.id_ss_vpn_cloudwatch_group\s*=\s*"([^"]+)"').replace("-", ""),
        "cloudwatch_group2_LGName": extract_value(python_code, r'self\.tag_name_ss_vpn_cloudwatch_group\s*=\s*"([^"]+)"'),
        "cloudwatch_group2_retention": int(extract_value(python_code, r'retention_in_days\s*=\s*([0-9]+)')),
        "cloudwatch_iam_role_quantity": len(re.findall(r'iam\.Role\(', python_code)),
        "cloudwatch__iam_role_tag_id": extract_value(python_code, r'self\.id_ss_vpn_cloudwatch_iam_role\s*=\s*"([^"]+)"').replace("-", ""),
        "cloudwatch_iam_role_name": extract_value(python_code, r'self\.tag_name_ss_vpn_cloudwatch_iam_role\s*=\s*"([^"]+)"'),
        "cloudwatch_iam_policy_quantity": len(re.findall(r'add_to_policy\(', python_code)),
        "cloudwatch_iam_policy_statements": "\n".join(re.findall(r'iam\.PolicyStatement\(\s*actions=\[([\s\S]*?)\],\s*resources',python_code)[0].strip().replace('"', '').split(",")),
        "vpn_connection_quantity": len(re.findall(r'ec2.CfnVPNConnection', python_code)),
        "vpn_connection_tag_id": extract_value(python_code, r'self\.id_ss_vpn_connection\s*=\s*"([^"]+)"').replace("-", ""),
        "vpn_connection_type": extract_value(python_code, r'type\s*=\s*"([^"]+)"'),
        "local_ipv4_network_cidr": extract_value(python_code, r'local_ipv4_network_cidr\s*=\s*"([^"]+)"'),
        "remote_ipv4_network_cidr": extract_value(python_code, r'remote_ipv4_network_cidr\s*=\s*"([^"]+)"'),

        # 9-f-1) Phase1EncryptionAlgorithms
        #"phase1_encryption_algorithms": extract_value(python_code, r'Phase1EncryptionAlgorithms\s*=\s*"([^"]+)"'),
        #"phase1_encryption_algorithms": extract_list_of_dicts(r'Phase1EncryptionAlgorithms\s*:\s*\[.*?\]')
        # "phase1_encryption_algorithms": r"Phase1EncryptionAlgorithms\s*=\s*\[\s*(.*?)\s*\]",
        # "phase2_encryption_algorithms": r"Phase2EncryptionAlgorithms\s*=\s*\[\s*(.*?)\s*\]",
        # "phase1_integrity_algorithms": r"Phase1IntegrityAlgorithms\s*=\s*\[\s*(.*?)\s*\]",
        # "phase2_integrity_algorithms": r"Phase2IntegrityAlgorithms\s*=\s*\[\s*(.*?)\s*\]",
        # "ike_versions": r"IKEVersions\s*=\s*\[\s*(.*?)\s*\]",
        # "log_enabled": r"LogEnabled\s*=\s*(True|False)",
        # "log_group_arn": r"LogGroupArn\s*=\s*([^\s,\}]+)"
        "vpn_tunnel_options": re.findall(r'VpnTunnelOptionsSpecifications\s*=\s*\[(.*?)\]', python_code, re.DOTALL),

        # 10- extract VPN Alarm SNS Topic from IaC
        "vpn_alarm_sns_topic_quantity": len(re.findall(r'sns.Topic', python_code)),
        "vpn_alarm_sns_topic_name": extract_value(python_code, r'topic_name\s*=\s*"([^"]+)"'),
        #11-
        "vpn_alarm_sns_subscription_quantity": len(re.findall(r'vpn_alarm_sns_topic.add_subscription', python_code)),
        "vpn_alarm_sns_subscription_email": extract_value(python_code, r'EmailSubscription\(\s*"([^"]+)"\s*\)'),
        # 12- extract_expected_values
        "tunnel1_alarm_quantity": len(re.findall(r'tunnel1_down_alarm', python_code)),
        "tunnel1_alarm_tag_id": extract_value(python_code, r'self\.id_ss_tunnel1_alarm\s*=\s*"([^"]+)"').replace("-", ""),
        "tunnel1_alarm_name": extract_value(python_code, r'alarm_name\s*=\s*"([^"]+)"'),
        "tunnel1_metric_name": extract_value(python_code, r'metric_name\s*=\s*"([^"]+)"'),
        "tunnel1_namespace": extract_value(python_code, r'namespace\s*=\s*"([^"]+)"'),
        "tunnel1_ip_address": extract_value(python_code, r'"TunnelIpAddress":\s*"([^"]+)"'),
        "tunnel1_statistic": extract_value(python_code, r'statistic\s*=\s*"([^"]+)"'),
        "tunnel1_period": int(extract_value(python_code, r'period=cdk\.Duration\.minutes\((\d+)\)')),
        "tunnel1_threshold": int(extract_value(python_code, r'threshold\s*=\s*(\d+)')),
        "tunnel1_evaluation_periods": int(extract_value(python_code, r'evaluation_periods\s*=\s*(\d+)')),
        "tunnel1_comparison_operator": extract_value(python_code, r'comparison_operator\s*=\s*cloudwatch\.ComparisonOperator\.([A-Z_]+)'),
        "tunnel1_datapoints_to_alarm": int(extract_value(python_code, r'datapoints_to_alarm\s*=\s*(\d+)')),
        "tunnel1_alarm_description": extract_value(python_code, r'alarm_description\s*=\s*"([^"]+)"'),







    }


# Fixture to extract expected values from Python code
@pytest.fixture(scope="module")
def expected_values(python_code):
    """
    Fixture to extract expected values from Python code.

    Args:
        python_code (str): Python IaC code content.

    Returns:
        dict: Extracted expected values.
    """
    return extract_expected_values(python_code)

def test_validate_transit_gateway(json_data, expected_values):
    """
    Test Case 1: Validate Transit Gateway
    """
    print("\n1. Validate Transit Gateway:")
    transit_gateways = [
        resource
        for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::EC2::TransitGateway"
    ]

    if not transit_gateways:
        pytest.fail("No Transit Gateway resource found in the JSON.")

    transit_gateway = transit_gateways[0]

    # 1- a) Check the Quantity of Transit Gateways
    actual_quantity = len(transit_gateways)
    expected_quantity = expected_values["transit_gateway_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("1- a) Check the Quantity of Transit Gateways", expected_quantity, actual_quantity, result))
    assert result

    # 1- b) Validate Tag Name
    expected_tag_name = expected_values["transit_gateway_tag_name"]
    result, actual_tag_name = validate_tag_name(transit_gateway, expected_tag_name)
    print(format_test_result("1- b) Validate Tag Name", expected_tag_name, actual_tag_name, result))
    assert result

    # 1- c) Validate Transit Gateway Tag ID
    expected_tag_id = expected_values["transit_gateway_tag_id"]
    actual_tag_id = next(
        key for key, resource in json_data["Resources"].items()
        if resource["Type"] == "AWS::EC2::TransitGateway"
    )
    result = actual_tag_id == expected_tag_id
    print(format_test_result("1- c) Validate Transit Gateway Tag ID", expected_tag_id, actual_tag_id, result))
    assert result

def test_validate_resource_share_tgw(json_data, expected_values):
    """
    Test Case 2: Validate Shared-Services-Resource-Share-TGW
    """
    print("\n2. Validate Shared-Services-Resource-Share-TGW:")
    resource_shares = [
        resource
        for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::RAM::ResourceShare"
        and resource["Properties"]["Name"] == "Shared-Services-Resource-Share-TGW"
    ]
    if not resource_shares:
        pytest.fail("No Shared-Services-Resource-Share-TGW resource found in the JSON.")
    resource_share = resource_shares[0]


    # 2- a) Check the Quantity of Shared-Services-Resource-Share-TGW
    actual_quantity = len(resource_shares)
    expected_quantity = expected_values["resource_share_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("2- a) Check the Quantity of Shared-Services-Resource-Share-TGW", expected_quantity, actual_quantity, result))
    assert result

    # 2-b) Validate Tag Name using the utility function
    expected_tag_name = expected_values["resource_share_tag_name"]
    result, actual_tag_name = validate_tag_name(resource_share, expected_tag_name)
    print(format_test_result("2-b) Validate Tag Name", expected_tag_name, actual_tag_name, result))
    assert result


     # 2- c) Validate Tag ID
    expected_tag_id = expected_values["resource_share_tag_id"]
    actual_tag_id = next(
        key for key, resource in json_data["Resources"].items()
        if resource["Type"] == "AWS::RAM::ResourceShare"
    )
    result = actual_tag_id == expected_tag_id
    print(format_test_result("2- c) Validate Resource Share Tag ID", expected_tag_id, actual_tag_id, result))
    assert result

    # 2- d) Validate Principals ARN
    actual_principals = resource_share["Properties"].get("Principals", [])
    expected_principal = expected_values["principal_arn"]
    result = expected_principal in actual_principals
    print(format_test_result("2- d) Validate Principals arn:aws:organizations", expected_principal, actual_principals, result))
    assert result

# Test case 3: Validate Shared Services Global Network
def test_validate_global_network(json_data: dict, expected_values: dict) -> None:
    """Test the validation of the Shared Services Global Network.

    Args:
        json_data (dict): The JSON data containing resources.
        expected_values (dict): The expected values extracted from the IaC.
    """
    print("\n3. Validate Shared Services Global Network:")

    global_networks = [
        resource for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::NetworkManager::GlobalNetwork"
    ]

    if not global_networks:
        pytest.fail("No Shared Services global network resource found in the JSON.")
    global_network = global_networks[0]

    # 3-a) Check the Quantity of Global Network
    actual_quantity = len(global_networks)
    expected_quantity = expected_values["global_network_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("3-a) Check the Quantity of Global Network", expected_quantity, actual_quantity, result))
    assert result

    # 3-b) Check the Name of the Global Network
    expected_tag_name = expected_values["global_network_tag_name"]
    result, actual_tag_name = validate_tag_name(global_network, expected_tag_name)
    print(format_test_result("3-b) Validate Tag Name", expected_tag_name, actual_tag_name, result))
    assert result


    # 3-c) Validate the Tag ID for the Global Network
    expected_id = expected_values["global_network_tag_id"]
    actual_id = next(
        (key for key, resource in json_data["Resources"].items()
         if resource["Type"] == "AWS::NetworkManager::GlobalNetwork"),
        None
    )
    result = actual_id == expected_id
    print(format_test_result("3-c) Validate the Tag ID of the Global Netwrok", expected_id, actual_id, result))
    assert result

    # 3-d) Check the Global Network Description
    expected_description = expected_values["global_network_description"]
    actual_description = global_network["Properties"]["Description"]
    result = actual_description == expected_description
    print(format_test_result("3-d) Check the Global Network Description", expected_description, actual_description, result))
    assert result


 # Test case 4: Validate Shared Services TGW Registration
def test_validate_tgw_registration(json_data: dict, expected_values: dict) -> None:
    """
    Test Case 4: Validate Shared Services TGW Registration.

    Args:
        json_data (dict): The JSON data containing resources.
        expected_values (dict): The expected values extracted from the IaC.
    """
    print("\n4. Validate Shared Services TGW Registration:")

    tgw_registrations = [
        resource for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::NetworkManager::TransitGatewayRegistration"
    ]

    if not tgw_registrations:
        pytest.fail("No Shared Services TGW Registration resource found in the JSON.")


    # 4-a) Check the Quantity of Shared Services TGW Registrations
    actual_quantity = len(tgw_registrations)
    expected_quantity = expected_values["tgw_registration_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("4-a) Check the Quantity of TGW Registrations", expected_quantity, actual_quantity, result))
    assert result

    # 4-b) Validate the Tag ID for TGW Registration
    expected_tag_id = expected_values["tgw_registration_tag_id"]
    actual_tag_id = next(
        (key for key, resource in json_data["Resources"].items()
            if resource["Type"] == "AWS::NetworkManager::TransitGatewayRegistration"),
        None
    )
    result = actual_tag_id == expected_tag_id
    print(
        format_test_result("4-b) Validate the Tag ID for TGW Registration", expected_tag_id, actual_tag_id, result))
    assert result

# Test Case 5: Validate Shared Services VPN Gateway
def test_validate_vpn_gateway(json_data: dict, expected_values: dict) -> None:
    """
    Test Case 5: Validate Shared Services VPN Gateway.

    Args:
        json_data (dict): The JSON data containing resources.
        expected_values (dict): The expected values extracted from the IaC.
    """
    print("\n5. Validate Shared Services VPN Gateway:")

    vpn_gateways = [
        resource for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::EC2::CustomerGateway"
    ]

    if not vpn_gateways:
        pytest.fail("No Shared Services VPN Gateway resource found in the JSON.")

    vpn_gateway = vpn_gateways[0]


    # 5-a) Check the Quantity of VPN Gateway
    actual_quantity = len(vpn_gateways)
    expected_quantity = expected_values["vpn_gateway_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("5-a) Check the Quantity of VPN Gateway", expected_quantity, actual_quantity, result))
    assert result

    # 5-b) Validate the Tag ID for VPN Gateway
    expected_tag_id = expected_values["vpn_gateway_tag_id"]
    actual_tag_id = next(
        key for key, resource in json_data["Resources"].items()
        if resource["Type"] == "AWS::EC2::CustomerGateway"
    )
    result = actual_tag_id == expected_tag_id
    print(format_test_result("5-b) Validate the Tag ID for VPN Gateway", expected_tag_id, actual_tag_id, result))
    assert result

    # 5-c) Validate the IP Address for VPN Gateway
    expected_ip_address = expected_values["vpn_gateway_ip_address"]
    actual_ip_address = vpn_gateway["Properties"]["IpAddress"]
    result = actual_ip_address == expected_ip_address
    print(format_test_result("5-c) Validate the IP Address for VPN Gateway", expected_ip_address, actual_ip_address, result))
    assert result

    # 5-d) Validate bgp_asn for the VPN Gateway
    expected_bgp_asn = expected_values["vpn_gateway_bgp_asn"]
    actual_bgp_asn = vpn_gateway["Properties"]["BgpAsn"]
    result = actual_bgp_asn == expected_bgp_asn
    print(format_test_result("5-d) Validate bgp_asn for the VPN Gateway", expected_bgp_asn, actual_bgp_asn, result))
    assert result

    # 5-e) Validate the Type of VPN Gateway
    expected_type = expected_values["vpn_gateway_type"]
    actual_type = vpn_gateway["Properties"]["Type"]
    result = actual_type == expected_type
    print(format_test_result("5-e) Validate the Type of VPN Gateway", expected_type, actual_type, result))
    assert result

def test_validate_cloudwatch_group2(json_data: dict, expected_values: dict):
    """
    Test Case 6: Validate Shared Services VPN Cloud Watch Group2
    """
    print("\n6. Validate Shared Services VPN Cloud Watch Group2:")
    cloudwatch_groups = [
        resource for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::Logs::LogGroup"
    ]
    if not cloudwatch_groups:
        pytest.fail("No Shared-Services-VPN Cloud Watch Group2 found in the JSON.")

    cloudwatch_group = cloudwatch_groups[0]

    # 6-a) Check the Quantity of VPN Cloud Watch Group2
    actual_quantity = len(cloudwatch_groups)
    expected_quantity = expected_values["cloudwatch_group2_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("6-a) Check the Quantity of VPN Cloud Watch Group2", expected_quantity, actual_quantity, result))
    assert result

    # 6-b) Check the Tag Name of the VPN Cloud Watch Group2
    expected_tag_name = expected_values["cloudwatch_group2_tag_name"]
    result, actual_tag_name = validate_tag_name(cloudwatch_group, expected_tag_name)
    print(format_test_result("6-b) Validate Tag Name", expected_tag_name, actual_tag_name, result))
    assert result

    # 6-c) Validate the Tag ID for the VPN Cloud Watch Group2
    expected_id = expected_values["cloudwatch_group2_tag_id"]
    actual_id = next(
        (key for key, resource in json_data["Resources"].items()
         if resource["Type"] == "AWS::Logs::LogGroup"),
        None
    )
    result = actual_id == expected_id
    print(format_test_result("6-c) Validate the Tag ID for the VPN Cloud Watch Group2", expected_id, actual_id, result))
    assert result

    # Test 6-d) Validate the Log Group Name for VPN Cloud Watch Group 2
    actual_log_group_name = cloudwatch_group["Properties"]["LogGroupName"]
    expected_log_group_name = expected_values["cloudwatch_group2_LGName"]
    result = actual_log_group_name == expected_log_group_name
    print(format_test_result("6-d) Validate the Log Group Name for VPN Cloud Watch Group 2", expected_log_group_name, actual_log_group_name, result))
    assert result

    # Test 6-e) Validate the Retention In Days for VPN Cloud Watch Group 2
    actual_retention = cloudwatch_group["Properties"]["RetentionInDays"]
    expected_retention = expected_values["cloudwatch_group2_retention"]
    result = actual_retention == expected_retention
    print(format_test_result("6-e) Validate the Retention In Days for VPN Cloud Watch Group 2", expected_retention, actual_retention, result))
    assert result

# Test Case 7: Validate Shared Services VPN Cloudwatch IAM Role
def test_validate_cloudwatch_iam_role(json_data: dict, expected_values: dict) -> None:
    """
    Test Case 7: Validate Shared Services VPN Cloudwatch IAM Role.

    """
    print("\n7. Validate Shared Services VPN Cloudwatch IAM Role:")

    iam_roles = [
        resource for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::IAM::Role"
        and resource["Properties"].get("RoleName") == "Shared-Services-VPN-Cloudwatch-IAM-Role"
    ]

    if not iam_roles:
        pytest.fail("No Shared Services VPN Cloudwatch IAM Role resource found in the JSON.")
    iam_role = iam_roles[0]

    # 7-a) Check the Quantity of VPN Cloudwatch IAM Role
    actual_quantity = len(iam_roles)
    expected_quantity = expected_values["cloudwatch_iam_role_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("7-a) Check the Quantity of VPN Cloudwatch IAM Role", expected_quantity, actual_quantity, result))
    assert result

    # 7-b) Validate the Tag ID for VPN Cloudwatch IAM Role
    expected_id = expected_values["cloudwatch__iam_role_tag_id"]
    actual_id = next(
    (re.sub(r'\d.*$', '', key) for key, resource in json_data["Resources"].items()
     if resource["Type"] == "AWS::IAM::Role"),
    None
    )
    result = actual_id == expected_id
    print(format_test_result("7-b) Validate the Tag ID for VPN Cloudwatch IAM Role", expected_id, actual_id, result))
    assert result

    # 7-c) Validate the Role Name for VPN Cloudwatch IAM Role
    expected_role_name = expected_values["cloudwatch_iam_role_name"]
    actual_role_name = iam_role["Properties"]["RoleName"]
    result = actual_role_name == expected_role_name
    print(format_test_result("7-c) Validate the Role Name for VPN Cloudwatch IAM Role", expected_role_name, actual_role_name, result))
    assert result

# Test Case 8: Validate Shared Services VPN Cloudwatch IAM Role Default Policy
def test_validate_cloudwatch_iam_role_default_policy(json_data: dict, expected_values: dict) -> None:
    """
    Test Case 8: Validate Shared Services VPN Cloudwatch IAM Role Default Policy.
    """
    print("\n8. Validate Shared Services VPN Cloudwatch IAM Role Default Policy:")

    iam_policies = [
        resource for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::IAM::Policy"
        and resource["Properties"].get("PolicyDocument") is not None
    ]

    if not iam_policies:
        pytest.fail("No Shared Services VPN Cloudwatch IAM Role Default Policy resource found in the JSON.")
    iam_policy = iam_policies[0]


    # 8-a) Check the Quantity of VPN Cloudwatch IAM Role Default Policy
    actual_quantity = len(iam_policies)
    expected_quantity = expected_values["cloudwatch_iam_policy_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("8-a) Check the Quantity of VPN Cloudwatch IAM Role Default Policy", expected_quantity, actual_quantity, result))
    assert result

    # 8-b) Check the Policy Statement for VPN Cloudwatch IAM Role Default Policy
    actual_policy_statements = [
        action for statement in iam_policy["Properties"]["PolicyDocument"]["Statement"]
        for action in (statement["Action"] if isinstance(statement["Action"], list) else [statement["Action"]])
    ]
    expected_policy_statements = expected_values["cloudwatch_iam_policy_statements"].split("\n")

    # Strip used to remove the empty lines
    # Sorted used to actions are compared irrespective of their order.
    cleaned_actual_policy_statements = sorted(action.strip() for action in actual_policy_statements if action.strip())
    cleaned_expected_policy_statements = sorted(action.strip() for action in expected_policy_statements if action.strip())
    result = cleaned_actual_policy_statements == cleaned_expected_policy_statements
    print(format_test_result("8-b) Check the Policy Statement for VPN Cloudwatch IAM Role Default Policy", cleaned_actual_policy_statements, cleaned_expected_policy_statements, result))
    assert result

#   # Test Case 9: Validate Shared Services VPN Connection
def test_validate_vpn_connection(json_data: dict, expected_values: dict) -> None:
    """
    Test Case 9: Validate Shared Services VPN Connection
    """
    print("\n9. Validate Shared Services VPN Gateway:")

    # Get all VPNConnection resources from the JSON
    resources = json_data.get("Resources", {})
    if not isinstance(resources, dict):
        pytest.fail("Invalid JSON structure: 'Resources' should be a dictionary.")

    vpn_connections = [
        resource for resource in resources.values()
        if resource.get("Type") == "AWS::EC2::VPNConnection"
    ]

    if not vpn_connections:
        pytest.fail("No Shared Services VPN Connection resource found in the JSON.")

    vpn_connection = vpn_connections[0]

    # 9-a: Check the Quantity of VPN Connection
    actual_quantity = len(vpn_connections)
    expected_quantity = expected_values["vpn_connection_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("9-a)Check the Quantity of VPN Connection", expected_quantity, actual_quantity, result))
    assert result

    # Test Case 9-b: Validate the Tag ID for VPN Connection
    expected_tag_id = expected_values.get("vpn_connection_tag_id", None)
    if expected_tag_id is None:
        pytest.fail("Key 'vpn_connection_tag_id' is missing in expected_values.")

    actual_tag_id = next(
        (key for key, resource in resources.items()
         if resource.get("Type") == "AWS::EC2::VPNConnection"), None
    )
    result = actual_tag_id == expected_tag_id
    print(format_test_result("Test Case 9-b: Validate the Tag ID for VPN Connection", expected_tag_id, actual_tag_id, result))
    assert result

    #  Test Case 9-c: Validate the type of VPN Connection
    expected_type = expected_values["vpn_connection_type"]
    actual_type = vpn_connection["Properties"]["Type"]
    result = actual_type == expected_type
    print(format_test_result("9-c) Validate the type of VPN Connection", expected_type, actual_type, result))
    assert result

    # 9-d) Validate local_ipv4_network_cidr for VPN Connection:
    expected_local_ipv4_network_cidr = expected_values["local_ipv4_network_cidr"]
    actual_local_ipv4_network_cidr = vpn_connection["Properties"]["LocalIpv4NetworkCidr"]
    result = actual_local_ipv4_network_cidr == expected_local_ipv4_network_cidr
    print(format_test_result("9-d) Validate local_ipv4_network_cidr for VPN Connection", expected_local_ipv4_network_cidr, actual_local_ipv4_network_cidr, result))
    assert result
    # 9-e) Validate remote_ipv4_network_cidr for VPN Connection
    expected_remote_ipv4_network_cidr = expected_values["remote_ipv4_network_cidr"]
    actual_remote_ipv4_network_cidr = vpn_connection["Properties"]["RemoteIpv4NetworkCidr"]
    result = actual_remote_ipv4_network_cidr == expected_remote_ipv4_network_cidr
    print(format_test_result("9-e) Validate remote_ipv4_network_cidr for VPN Connection", expected_remote_ipv4_network_cidr, actual_remote_ipv4_network_cidr, result))
    assert result

"""
    # 9-f-1: Validate Phase1EncryptionAlgorithms for VPN Connection
    expected_algorithms = expected_values["vpn_tunnel_options"]
    phase1_encryption_algorithms = vpn_connection["Properties"]["VpnTunnelOptionsSpecifications"][0]["Phase1EncryptionAlgorithms"]
    result = sorted(phase1_encryption_algorithms) == sorted(expected_algorithms)
    print(format_test_result("9-f-1) Validate Phase1EncryptionAlgorithms for VPN Connection", expected_algorithms, phase1_encryption_algorithms, result))
    assert result

    # 9-f): Validate Vpn Tunnel Options Specifications
    expected_vpn_tunnel_options = expected_values["vpn_tunnel_options"]
    actual_vpn_tunnel_options = vpn_connection["Properties"]['VpnTunnelOptionsSpecifications']
    result = expected_vpn_tunnel_options == actual_vpn_tunnel_options
    print(format_test_result("9-f) Validate VpnTunnelOptionsSpecifications", expected_vpn_tunnel_options, actual_vpn_tunnel_options, result))
    assert result, "Test failed due to mismatch between expected and actual VPN tunnel options."
"""

# Test case 10 - Validate VPN Alarm SNS Topic
def test_validate_vpn_alarm_sns_topic(json_data: dict, expected_values: dict) -> None:
    """
    Test case 10 - Validate VPN Alarm SNS Topic
    """
    print("\n10. Test case 10 - Validate VPN Alarm SNS Topic:")

    # Extract all SNS Topic resources from the JSON
    sns_topics = [
        resource for resource in json_data.get("Resources", {}).values()
        if resource.get("Type") == "AWS::SNS::Topic"
    ]
    sns_topic = sns_topics[0]

    # 10-a) Check the quantity of SNS Topics
    expected_quantity = expected_values["vpn_alarm_sns_topic_quantity"]
    actual_quantity = len(sns_topics)
    result = actual_quantity == expected_quantity
    print(format_test_result("10-a) Check the Quantity of VPN Alarm SNS Topics", expected_quantity, actual_quantity, result))
    assert result

    # 10-b) Validate the topic_name for VPN Alarm SNS Topic
    expected_topic_name = expected_values["vpn_alarm_sns_topic_name"]
    actual_topic_name = sns_topic["Properties"]["TopicName"]
    result = actual_topic_name == expected_topic_name
    print(format_test_result("10-b) Validate the topic_name for VPN Alarm SNS Topic", expected_topic_name, actual_topic_name, result))
    assert result

# Test case 11 - Validate VPN Alarm SNS Subscription
def test_validate_vpn_alarm_sns_subscription(json_data: dict, expected_values: dict) -> None:
    """
    Test case 11 - Validate VPN Alarm SNS Subscription
    """
    print("\n11. Test case 11 - Validate VPN Alarm SNS Subscription:")

    # Extract all SNS Subscription resources from the JSON
    sns_subscriptions = [
        resource for resource in json_data.get("Resources", {}).values()
        if resource.get("Type") == "AWS::SNS::Subscription"
    ]
    sns_subscription = sns_subscriptions[0]

    # 11-a) Check the quantity of SNS Subscriptions
    expected_quantity = expected_values["vpn_alarm_sns_subscription_quantity"]
    actual_quantity = len(sns_subscriptions)
    result = actual_quantity == expected_quantity
    print(format_test_result("11-a) Check the Quantity of VPN Alarm SNS Subscriptions", expected_quantity, actual_quantity, result))
    assert result

    # 11-b) Validate the email address for the SNS Subscription
    expected_email = expected_values["vpn_alarm_sns_subscription_email"]
    actual_email = sns_subscription["Properties"]["Endpoint"]
    result = actual_email == expected_email
    print(format_test_result("11-b) Validate the email address for VPN Alarm SNS Subscription", expected_email, actual_email, result))
    assert result




# Completion message
def test_completion():
    """
    Print a message indicating that all tests have been completed.
    """
    print("Tests completed.")

######################################################################################################################


def test_validate_tunnel1_alarm(json_data: dict, expected_values: dict) -> None:
    """
    Test Case 12 - Validate Shared Services Tunnel 1 Alarm
    """
    print("\n12. Validate Shared Services Tunnel 1 Alarm:")

    # Extract the Tunnel 1 alarms from JSON
    tunnel1_alarms = [
        resource for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::CloudWatch::Alarm"
    ]
    if not tunnel1_alarms:
        pytest.fail("No Shared-Services-tunnel1_alarm resource found in the JSON.")
    tunnel1_alarm = tunnel1_alarms[0]

    # 12-a) Check the Quantity of Tunnel Alarms
    expected_quantity = expected_values["tunnel1_alarm_quantity"]
    actual_quantity = len(tunnel1_alarms)
    result = actual_quantity == expected_quantity
    print(format_test_result("12-a) Check the Quantity of Tunnel Alarms", expected_quantity, actual_quantity, result))
    assert result

    # 12-b) Validate the Tag ID for Tunnel Alarm
    expected_tag_id = expected_values["tunnel1_alarm_tag_id"]
    actual_tag_id = next(
        key for key, resource in json_data["Resources"].items()
        if resource["Type"] == "AWS::CloudWatch::Alarm"
    )
    actual_tag_id = re.sub(r'Alar[m].*$', 'Alarm', actual_tag_id)  # Remove everything after 'Alarm'
    result = actual_tag_id == expected_tag_id
    print(format_test_result("12-b) Validate the Tag ID for Tunnel Alarm", expected_tag_id, actual_tag_id, result))
    assert result


    # 12-c) Validate the alarm_name for Tunnel Alarm
    actual_alarm_name = tunnel1_alarm["Properties"]["AlarmName"]
    expected_alarm_name = expected_values["tunnel1_alarm_name"]
    result = actual_alarm_name == expected_alarm_name
    print(format_test_result("12-c) Validate the alarm_name for Tunnel Alarm", expected_alarm_name, actual_alarm_name, result))
    assert result

    # 12-d) Validate the metric_name for Tunnel Alarm
    actual_metric_name = tunnel1_alarm["Properties"]["MetricName"]
    expected_metric_name = expected_values["tunnel1_metric_name"]
    result = actual_metric_name == expected_metric_name
    print(format_test_result("12-d) Validate the metric_name for Tunnel Alarm", expected_metric_name, actual_metric_name, result))
    assert result

    # 12-e) Validate namespace for Tunnel Alarm
    actual_namespace = tunnel1_alarm["Properties"]["Namespace"]
    expected_namespace = expected_values["tunnel1_namespace"]
    result = actual_namespace == expected_namespace
    print(format_test_result("12-e) Validate namespace for Tunnel Alarm", expected_namespace, actual_namespace, result))
    assert result

    # 12-f) Validate TunnelIpAddress
    tunnel_ip_dimension = next((dim for dim in tunnel1_alarm["Properties"]["Dimensions"]
                                if dim["Name"] == "TunnelIpAddress"), {})
    actual_tunnel_ip = tunnel_ip_dimension.get("Value", None)
    expected_tunnel_ip = expected_values["tunnel1_ip_address"]
    result = actual_tunnel_ip == expected_tunnel_ip
    print(format_test_result("12-f) Validate TunnelIpAddress", expected_tunnel_ip, actual_tunnel_ip, result))
    assert result

    # 12-g) Validate statistic
    actual_statistic = tunnel1_alarm["Properties"]["Statistic"]
    expected_statistic = expected_values["tunnel1_statistic"]
    result = actual_statistic == expected_statistic
    print(format_test_result("12-g) Validate statistic", expected_statistic, actual_statistic, result))
    assert result

    # # 12-h) Check the period from Tunnel Alarm
    # actual_period = tunnel1_alarm["Properties"]["Period"]
    # expected_period = expected_values["tunnel1_period"]
    # result = actual_period == expected_period
    # print(format_test_result("12-h) Check the period from Tunnel Alarm", expected_period, actual_period, result))
    # assert result

    # 12-i) Check the threshold from Tunnel Alarm
    actual_threshold = tunnel1_alarm["Properties"]["Threshold"]
    expected_threshold = expected_values["tunnel1_threshold"]
    result = actual_threshold == expected_threshold
    print(format_test_result("12-i) Check the threshold from Tunnel Alarm", expected_threshold, actual_threshold, result))
    assert result

    # 12-j) Validate evaluation_periods
    actual_evaluation_periods = tunnel1_alarm["Properties"]["EvaluationPeriods"]
    expected_evaluation_periods = expected_values["tunnel1_evaluation_periods"]
    result = actual_evaluation_periods == expected_evaluation_periods
    print(format_test_result("12-j) Validate evaluation_periods", expected_evaluation_periods, actual_evaluation_periods, result))
    assert result

    # 12-k) Validate comparison_operator from Tunnel Alarm
    actual_comparison_operator = tunnel1_alarm["Properties"]["ComparisonOperator"].upper().replace('_', '')
    expected_comparison_operator = expected_values["tunnel1_comparison_operator"].upper().replace('_', '')
    result = actual_comparison_operator == expected_comparison_operator
    print(format_test_result("12-k) Validate comparison_operator from Tunnel Alarm", expected_comparison_operator, actual_comparison_operator, result))
    assert result

    # 12-l) Validate datapoints_to_alarm
    actual_datapoints_to_alarm = tunnel1_alarm["Properties"]["DatapointsToAlarm"]
    expected_datapoints_to_alarm = expected_values["tunnel1_datapoints_to_alarm"]
    result = actual_datapoints_to_alarm == expected_datapoints_to_alarm
    print(format_test_result("12-l) Validate datapoints_to_alarm", expected_datapoints_to_alarm, actual_datapoints_to_alarm, result))
    assert result

    # 12-m) Validate alarm_description
    actual_alarm_description = tunnel1_alarm["Properties"]["AlarmDescription"]
    expected_alarm_description = expected_values["tunnel1_alarm_description"]
    result = actual_alarm_description == expected_alarm_description
    print(format_test_result("12-m) Validate alarm_description", expected_alarm_description, actual_alarm_description, result))
    assert result