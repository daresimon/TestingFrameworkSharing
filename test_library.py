import pytest
from data_driven.mockServer import mockServerData
from assertpy import assert_that
import allure

'''
Split out common functions into separate functions that can be called in test cases
-> Increase reusability
-> Decrease code length
-> Easier to modify common function 

Example: 
1.  [Add User] function used in test case to check for increase in users in server
2.  [Add User] function used in test case to check added information are correct
3.  [Add User] function used in test case to check if added user can be deleted
4.  [Add User] function used in test to check if added user can be edited

-> [Add User] taken out from individual test case and made into a function itself that can be called for test cases
    -> If [Add User] require new information, just need to edit addUser function

Difference with Modular Framework: 
Modular framework split application into modules based on its feature
    -> Everything related to test [add user] is one module 
Library Architecture Framework takes out common functions to create into separate, callable functions 
    -> Everything that requires [add user] uses that function 
'''

#Set up object to act as 'Server' to retrieve and input data
@pytest.fixture()
def server():
    server = mockServerData('getUser')
    return server

def addUser(server):
    add_user_data = {
            'name': 'newUser',
            'userID': 2345,
            'email': 'newUser@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'#,
            #'joining_date': '2020-09-23' #Newly added data type
        }
    server.serverData.append(add_user_data)

def test_addUserAndCheckNumber(server):
    addUser(server)
    assert_that(len(server.serverData)).is_equal_to(2)

def test_addUserAndCheckInfo(server):
    addUser(server)
    added_user_data = {
            'name': 'newUser',
            'userID': 2345,
            'email': 'newUser@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    assert_that(server.serverData[1]).is_equal_to(added_user_data)

def test_addUserAndDelete(server):
    addUser(server)
    del server.serverData[-1]
    assert_that(len(server.serverData)).is_equal_to(1)

def test_addUserAndEdit(server):
    addUser(server)
    server.serverData[1]["name"] = "Changed Name"
    assert_that(server.serverData[1].get("name")).is_equal_to("Changed Name")