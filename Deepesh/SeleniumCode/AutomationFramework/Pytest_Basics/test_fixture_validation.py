"""
# Fixture : Fixture something that helps to do initial setup and teardown of the test cases.
@pytest.mark.fixture(scope='function')
def fun_name()

Function : -> Function fixture is limited to each test function.
           -> Function fixture executes before and after execution of each test function.

Module :  ->  Module level fixture works with each module file.
          -> Module level fixture will execute before execution of all test cases and
             after completion of all the test cases in module.
package :  ->  Package fixture will work with all files in the specified package.
           ->  Package level fixture will execute before execution of test module.

session :  ->  Session fixture when we initiate the session of automation.
           ->  Session fixture has higher priority as compare to all other fixtures.
class :

"""
import pytest


@pytest.fixture(scope="function", autouse=True)
def fun_fixture():
    print("\n------Initiate function fixture----")
    yield
    print("\n------completed function fixture----")


@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    print("\n------Initiate module fixture----")
    yield
    print("\n------completed module fixture----")


@pytest.fixture(scope="package", autouse=True)
def package_fixture():
    print("\n------Initiate Package fixture----")
    yield
    print("\n------completed Package fixture----")

@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("\n------Initiate Session fixture----")
    yield
    print("\n------completed Session fixture----")

def test_addition():
    num1 = 50
    num2 = 60
    assert num1 + num2 == 110


def test_multiplication():
    num1 = 500
    num2 = 7
    assert num1 * num2 == 4000


def test_subtraction():
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200


def test_divide():
    n1 = 500
    n2 = 10
    assert n1 // n2 == 400
