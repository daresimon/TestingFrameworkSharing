import pytest
from data_driven.mockServer import mockServerData
from assertpy import assert_that
import allure

'''
Separated into modules according to feature so that if a feature is changed, only that module has to be edited
--> Easier to maintain and improve code

Example: Test case for adding a new user and checking whether the newly added information are correct

Without separation, [add] and [check] features combined in one test case
-> Eg [Add user] feature updated to include [permission] requirement
-> Test case have to be edited for both [add] and [check], and [check] feature has to account for different outcomes depending on permission

With separation, [add] and [check] features are separated modules
-> Eg [permission] requirement
-> Test case for [add] is edited, [check] feature can remain since the feature is not affected

**Potential Issue: Can [Add] and [Check] features be completely separated? 
-> If possible, no issue
-> For this case, it might not be ideal as the test data is required in different scripts and cannot be destroyed at the end of the test case
    -> Issues with test data maintenance
'''

#Set up object to act as 'Server' to retrieve and input data
@pytest.fixture()
def server():
    server = mockServerData('getUser')
    return server

#Without Separation
@allure.feature("before_change")
def test_addUserAndCheck(server):
    add_user_data = {
            'name': 'newUser',
            'userID': 2345,
            'email': 'newUser@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    server.serverData.append(add_user_data)
    assert_that(add_user_data).is_equal_to(server.serverData[1])

@allure.feature("after_change")
def test_addUserAndCheck(server):
    add_user_data = {
            'name': 'newUser',
            'userID': 2345,
            'email': 'newUser@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    if server.addPermission == 'yes':
        server.serverData.append(add_user_data)
    assert_that(add_user_data).is_equal_to(server.serverData[1])
    #No problem if it succeed. But if it fails, could the issue be because of not having permission, 
    #or certain added information does not tally because of an issue with the add feature?
        

#With Separation
separationCaseServer = mockServerData("getUser")

@allure.feature("before_change")
def test_addUser():
    num_users = len(separationCaseServer.serverData)
    add_user_data = {
            'name': 'newUser2',
            'userID': 2345,
            'email': 'newUser2@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    separationCaseServer.serverData.append(add_user_data)
    assert_that(len(separationCaseServer.serverData)).is_equal_to(num_users + 1)

@allure.feature("after_change")
def test_addUserWithPermission():
    num_users = len(separationCaseServer.serverData)
    add_user_data = {
            'name': 'newUser2',
            'userID': 2345,
            'email': 'newUser2@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    if separationCaseServer.addPermission == 'yes':
        separationCaseServer.serverData.append(add_user_data)
    assert_that(len(separationCaseServer.serverData)).is_equal_to(num_users + 1)

#Should be separated to another script for easier maintenance
def test_checkUser():
    check_user_data = {
            'name': 'newUser2',
            'userID': 2345,
            'email': 'newUser2@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    assert_that(separationCaseServer.serverData[1]).is_equal_to(check_user_data)


