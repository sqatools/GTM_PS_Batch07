"""
Unit tests for validating the configuration of AWS Transit Gateway and Resource Share
using pytest. This module includes tests to ensure that the expected resources and
properties are defined correctly in the provided JSON and Python IaC code.
"""
import json
import re  # to use re library for searching pattern in text
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
        "global_network_tag_id": extract_value(python_code, r'self\.id_ss_global_network\s*=\s*"([^"]+)"').replace("-",
                                                                                                                   ""),
        "global_network_description": extract_value(python_code, r'self\.tag_name_ss_global_network\s*=\s*"([^"]+)"'),
        "tgw_registration_quantity": len(re.findall(r'networkmanager\.CfnTransitGatewayRegistration', python_code)),
        "tgw_registration_tag_id": extract_value(python_code, r'self\.id_ss_tgw_registration\s*=\s*"([^"]+)"').replace(
            "-", ""),
        "vpn_gateway_quantity": len(re.findall(r'ec2\.CfnCustomerGateway', python_code)),
        "vpn_gateway_tag_id": extract_value(python_code, r'self\.id_ss_customer_gw\s*=\s*"([^"]+)"').replace("-", ""),
        "vpn_gateway_ip_address": extract_value(python_code, r'ip_address\s*=\s*"([^"]+)"'),
        "vpn_gateway_bgp_asn": int(extract_value(python_code, r'bgp_asn\s*=\s*(\d+)')),
        "vpn_gateway_type": extract_value(python_code, r'type\s*=\s*"([^"]+)"'),
        "cloudwatch_group2_quantity": len(re.findall(r'logs\.CfnLogGroup', python_code)),
        "cloudwatch_group2_tag_name": extract_value(python_code,
                                                    r'self\.tag_name_ss_vpn_cloudwatch_group\s*=\s*"([^"]+)"'),
        "cloudwatch_group2_tag_id": extract_value(python_code,
                                                  r'self\.id_ss_vpn_cloudwatch_group\s*=\s*"([^"]+)"').replace("-", ""),
        "cloudwatch_group2_LGName": extract_value(python_code,
                                                  r'self\.tag_name_ss_vpn_cloudwatch_group\s*=\s*"([^"]+)"'),
        "cloudwatch_group2_retention": int(extract_value(python_code, r'retention_in_days\s*=\s*([0-9]+)')),
        "cloudwatch_iam_role_quantity": len(re.findall(r'iam\.Role\(', python_code)),
        "cloudwatch__iam_role_tag_id": extract_value(python_code,
                                                     r'self\.id_ss_vpn_cloudwatch_iam_role\s*=\s*"([^"]+)"').replace(
            "-", ""),
        "cloudwatch_iam_role_name": extract_value(python_code,
                                                  r'self\.tag_name_ss_vpn_cloudwatch_iam_role\s*=\s*"([^"]+)"'),
        "cloudwatch_iam_policy_quantity": len(re.findall(r'add_to_policy\(', python_code)),
        "cloudwatch_iam_policy_statements": "\n".join(
            re.findall(r'iam\.PolicyStatement\(\s*actions=\[([\s\S]*?)\],\s*resources', python_code)[0].strip().replace(
                '"', '').split(",")),

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
    print(
        format_test_result("1- a) Check the Quantity of Transit Gateways", expected_quantity, actual_quantity, result))
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
    print(format_test_result("2- a) Check the Quantity of Shared-Services-Resource-Share-TGW", expected_quantity,
                             actual_quantity, result))
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
    print(format_test_result("2- d) Validate Principals arn:aws:organizations", expected_principal, actual_principals,
                             result))
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
    print(format_test_result("3-d) Check the Global Network Description", expected_description, actual_description,
                             result))
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
    print(
        format_test_result("4-a) Check the Quantity of TGW Registrations", expected_quantity, actual_quantity, result))
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
    print(format_test_result("5-c) Validate the IP Address for VPN Gateway", expected_ip_address, actual_ip_address,
                             result))
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
    print(format_test_result("6-a) Check the Quantity of VPN Cloud Watch Group2", expected_quantity, actual_quantity,
                             result))
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
    print(format_test_result("6-d) Validate the Log Group Name for VPN Cloud Watch Group 2", expected_log_group_name,
                             actual_log_group_name, result))
    assert result

    # Test 6-e) Validate the Retention In Days for VPN Cloud Watch Group 2
    actual_retention = cloudwatch_group["Properties"]["RetentionInDays"]
    expected_retention = expected_values["cloudwatch_group2_retention"]
    result = actual_retention == expected_retention
    print(format_test_result("6-e) Validate the Retention In Days for VPN Cloud Watch Group 2", expected_retention,
                             actual_retention, result))
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
    print(format_test_result("7-a) Check the Quantity of VPN Cloudwatch IAM Role", expected_quantity, actual_quantity,
                             result))
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
    print(format_test_result("7-c) Validate the Role Name for VPN Cloudwatch IAM Role", expected_role_name,
                             actual_role_name, result))
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
    print(format_test_result("8-a) Check the Quantity of VPN Cloudwatch IAM Role Default Policy", expected_quantity,
                             actual_quantity, result))
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
    cleaned_expected_policy_statements = sorted(
        action.strip() for action in expected_policy_statements if action.strip())
    result = cleaned_actual_policy_statements == cleaned_expected_policy_statements
    print(format_test_result("8-b) Check the Policy Statement for VPN Cloudwatch IAM Role Default Policy",
                             cleaned_actual_policy_statements, cleaned_expected_policy_statements, result))
    assert result


# Completion message
def test_completion():
    """
    Print a message indicating that all tests have been completed.
    """
    print("Tests completed.")
