'''
Overview of the project

For building infrastructure in AWS we have used IaC (Infrastructure as Code) so that if anything fails we can deploy the exact same again using code.
 We are doing this in AWS using CDK (Cloud Development Kit) and it will be written in Python. The python code, when synthesized, creates a JSON template
 that is passed to AWS Cloudformation to build the infrastructure based on the template. We need to test that the python code is creating the template correctly
 against the code. This will include, but not limited to, testing the tag names, ID’s, CIDRs/IP addresses and specific variables set in the code as well as correct
 quantities of infrastructure will be created. This will need to be done using pytest and will pass or fail the template prior to deployment to Cloudformation.

Requirements

The tests must be written in Python using Pytest

The test cases must be stored in TestRail

The tests must confirm that the JSON template has been created as per the IaC. These must include:

Quantities

Values

Parameters

Variables

A test plan must be created

A test design must be created

Test cases must be created

The python tests must have a Pylint score above 9

'''






import pytest
import json
import re


# Utility function to format test results
def format_test_result(test_name, expected, actual, result):
    """Format test results for clear output."""
    output = "Test Pass" if result else f"Test Fail - Expected {expected} but got {actual}"
    return f"\n{test_name}:\nExpected Result: {expected}\nActual Result: {actual}\nOutput: {output}"


# Load JSON file
@pytest.fixture(scope="module")
def json_data():
    """Load the JSON data from the template file."""
    json_file_path = "/home/ubuntu/shared-services-transit-gateway-stack/shared-services-transit-gateway-stack.template.json"
    try:
        with open(json_file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        pytest.fail(f"JSON file not found: {json_file_path}")
    except json.JSONDecodeError as e:
        pytest.fail(f"Failed to parse JSON file: {e}")


# Load Python IaC code
@pytest.fixture(scope="module")
def python_code_content():
    """Load the Python IaC code from the specified file."""
    python_file_path = "/home/ubuntu/shared-services-transit-gateway-stack/shared_services_transit_gateway_stack/shared_services_transit_gateway_stack.py"
    try:
        with open(python_file_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        pytest.fail(f"Python file not found: {python_file_path}")


# Extract values from Python IaC code using regex
def extract_value(content, pattern):
    """Extract a value from the Python IaC code using regex."""
    match = re.search(pattern, content)
    return match.group(1) if match else None


# Extract expected values from Python code
@pytest.fixture(scope="module")
def expected_values(python_code_content):
    """Extract expected values from the Python IaC code."""
    return {
        "transit_gateway_id": extract_value(python_code_content, r'self\.id_ss_tgw\s*=\s*"([^"]+)"'),
        "resource_share_quantity": int(
            extract_value(python_code_content, r'share_quantity\s*=\s*(\d+)') or 0
        ),
        "resource_share_tag_name": extract_value(
            python_code_content, r'self\.tag_name_ss_ram_share\s*=\s*"([^"]+)"'
        ),
        "resource_share_id": extract_value(
            python_code_content, r'self\.id_ss_ram_share\s*=\s*"([^"]+)"'
        ),
        "principal_arn": extract_value(
            python_code_content, r'self\.id_ss_organisation\s*=\s*"([^"]+)"'
        ),
    }


# Test Case 1: Validate Transit Gateway
def test_validate_transit_gateway(json_data, expected_values):
    print("\n1. Validate Transit Gateway:")

    # Extracting Transit Gateway resource from JSON
    transit_gateways = [
        resource
        for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::EC2::TransitGateway"
    ]

    # (a) Quantity of Transit Gateways
    actual_quantity = len(transit_gateways)
    expected_quantity = 1  # Replace with a specific value if known
    result = actual_quantity == expected_quantity
    print(
        format_test_result("1- a) Check the Quantity of Transit Gateways", expected_quantity, actual_quantity, result))
    assert result

    # If no transit gateway, fail early
    if not transit_gateways:
        pytest.fail("No Transit Gateway resource found in the JSON.")

    transit_gateway = transit_gateways[0]

    # (b) Validate Tag Name
    actual_tag_name = next(
        (tag["Value"] for tag in transit_gateway["Properties"]["Tags"] if tag["Key"] == "Name"),
        None,
    )
    expected_tag_name = "Shared-Services-Transit-Gateway"
    result = actual_tag_name == expected_tag_name
    print(format_test_result("1- b) Validate Tag Name", expected_tag_name, actual_tag_name, result))
    assert result

    # (c) Validate Tag ID
    actual_id = None

    # Extract the TransitGatewayId from the JSON
    if isinstance(transit_gateway["Properties"].get("TransitGatewayId", None), dict):
        fn_get_att = transit_gateway["Properties"]["TransitGatewayId"]
        if fn_get_att.get("Fn::GetAtt"):
            # Logical ID is the first element of Fn::GetAtt
            actual_id = fn_get_att["Fn::GetAtt"][0]

    # The expected ID from Python IaC (removing hyphens)
    expected_id = expected_values["transit_gateway_id"].replace("-", "")

    # Debugging output
    print(f"Expected ID (hyphens removed): {expected_id}")
    print(f"Actual ID (from JSON): {actual_id}")

    # Compare expected and actual
    result = actual_id == expected_id
    print(format_test_result("1- c) Validate Tag ID", expected_id, actual_id, result))
    assert result


# Test Case 2: Validate Shared-Services-Resource-Share-TGW
def test_validate_shared_services_resource_share_tgw(json_data, expected_values):
    print("\n2. Validate Shared-Services-Resource-Share-TGW:")

    # Extracting Shared-Services-Resource-Share-TGW from JSON
    resource_shares = [
        resource
        for resource in json_data["Resources"].values()
        if resource["Type"] == "AWS::RAM::ResourceShare"
           and resource["Properties"]["Name"] == "Shared-Services-Resource-Share-TGW"
    ]

    # (a) Quantity of Shared-Services-Resource-Share-TGW
    actual_quantity = len(resource_shares)
    expected_quantity = expected_values["resource_share_quantity"]
    result = actual_quantity == expected_quantity
    print(format_test_result("2- a) Check the Quantity of Shared-Services-Resource-Share-TGW", expected_quantity,
                             actual_quantity, result))
    assert result

    # If no resource share, fail early
    if not resource_shares:
        pytest.fail("No Shared-Services-Resource-Share-TGW resource found in the JSON.")

    resource_share = resource_shares[0]

    # (b) Validate Tag Name
    actual_tag_name = resource_share["Properties"]["Name"]
    expected_tag_name = expected_values["resource_share_tag_name"]
    result = actual_tag_name == expected_tag_name
    print(format_test_result("2- b) Validate Tag Name", expected_tag_name, actual_tag_name, result))
    assert result

    # (c) Validate Tag ID
    actual_id = resource_share["Properties"].get("ResourceShareId", None)
    expected_id = expected_values["resource_share_id"]
    result = actual_id == expected_id
    print(format_test_result("2- c) Validate Tag ID", expected_id, actual_id, result))
    assert result

    # (d) Validate Principals ARN
    actual_principals = resource_share["Properties"].get("Principals", [])
    expected_principal = expected_values["principal_arn"]
    result = expected_principal in actual_principals
    print(format_test_result("2- d) Validate Principals arn:aws:organizations", expected_principal, actual_principals,
                             result))
    assert result


# Completion message
def test_completion():
    print("\nTests completed.")
