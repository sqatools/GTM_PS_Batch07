import pytest

@pytest.mark.usefixtures("greeting")
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
