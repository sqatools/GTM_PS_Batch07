"""
# Fixture : Fixture something that helps to do initial setup and teardown of the test cases.
@pytest.mark.fixture(scope='function')
def fun_name()

Function :
Module
package
session
class

"""
import pytest


@pytest.fixture(scope="function", autouse=True)
def fun_fixture():
    print("\n------initiate fun fixture----")
    yield
    print("\n------completed fun fixture----")


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
