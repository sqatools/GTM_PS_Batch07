import pytest


@pytest.mark.smoke
def test_addition():
    num1 = 50
    num2 = 60
    assert num1 + num2 == 110


@pytest.mark.smoke
def test_multiplication():
    num1 = 500
    num2 = 7
    assert num1 * num2 == 4000


@pytest.mark.smoke
@pytest.mark.sanity
def test_subtraction():
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200


@pytest.mark.sanity
def test_divide():
    n1 = 500
    n2 = 10
    assert n1 // n2 == 400


@pytest.mark.sanity
@pytest.mark.regression
def test_addition_fun1():
    num1 = 50
    num2 = 60
    assert num1 + num2 == 110


@pytest.mark.regression
def test_multiplication_fun2():
    num1 = 500
    num2 = 7
    assert num1 * num2 == 4000


@pytest.mark.regression
@pytest.mark.functional
def test_subtraction_fun3():
    n1 = 500
    n2 = 300
    assert n1 - n2 == 200


@pytest.mark.functional
def test_divide_fun4():
    n1 = 500
    n2 = 10
    assert n1 // n2 == 400
