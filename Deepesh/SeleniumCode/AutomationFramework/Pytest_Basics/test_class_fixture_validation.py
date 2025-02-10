"""
# Fixture : Fixture something that helps to do initial setup and teardown of the test cases.
@pytest.mark.fixture(scope='function')
def fun_name()
class : 

"""
import pytest

@pytest.fixture(scope="class")
def class_fixture():
    print("--- class fixture initiated---")
    yield
    print("--- class fixture completed---")



@pytest.mark.usefixtures("class_fixture")
class TestMathOperation:
    def test_addition(self):
        num1 = 50
        num2 = 60
        assert num1 + num2 == 110

    def test_multiplication(self):
        num1 = 500
        num2 = 7
        assert num1 * num2 == 4000

    def test_subtraction(self):
        n1 = 500
        n2 = 300
        assert n1 - n2 == 200

    def test_divide(self):
        n1 = 500
        n2 = 10
        assert n1 // n2 == 400
