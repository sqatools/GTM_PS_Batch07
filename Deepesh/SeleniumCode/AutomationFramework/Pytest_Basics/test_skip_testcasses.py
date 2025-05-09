import pytest

ENV = "PROD"

def test_addition():
    num1 = 50
    num2 = 60
    assert num1 + num2 == 110

@pytest.mark.skip(reason='Not stable')
def test_multiplication():
    num1 = 500
    num2 = 7
    assert num1 * num2 == 4000


def test_subtraction():
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200


@pytest.mark.skipif(ENV == 'PROD', reason="Can not execute on production env")
def test_divide():
    n1= 500
    n2 = 10
    assert n1//n2 == 400
