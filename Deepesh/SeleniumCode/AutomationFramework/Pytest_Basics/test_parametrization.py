import pytest
from data_file import *


@pytest.mark.parametrize("username, password", [('user1', 'password1'),
                                                ('user2', 'Pa@ssword'),
                                                ('user3', 'P@ssw0rd3')])
def test_login(username, password):
    db_username = 'user2'
    db_password = 'Pa@ssword'
    if username == db_username and password == db_password:
        print("Login Successful")
    else:
        print("Invalid username password")


@pytest.mark.parametrize("username, password", user_cred_list)
def test_login2(username, password):
    db_username = 'user2'
    db_password = 'Pa@ssword'
    if username == db_username and password == db_password:
        print("Login Successful")
        assert True
    else:
        print("Invalid username password")
        assert False
