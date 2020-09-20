import pytest
from mockServer import mockServerData
from assertpy import assert_that
import allure
from data_driven.configured_data import setUser, multipleUsers

'''
Separate test case logic and data into separate scripts
-> need more time for planning
-> much shorter code base and easier to maintain

Example:
1.  Shorter code base
2.  Variables to represent data --> Can parametrize -> also leads to shorter code base
3.  Easy to see and change test data type

For changing test data's VALUE:
-> Easy to maintain test data
    -> everything can be referred to in one CSV file
    -> for eg, test data changes any value, changes can be made in CSV file instead of having to find the test data in test script and make the changes
    -> especially helpful if bulk changes occurs
-> No changes required for test script
    -> for eg, if test data changes but type does not change, no changes have to be made to the test script

For changing test data's TYPE:
-> Lesser touch points in test script
    -> for eg, if a variable's type changed, only need to change the test case logic, configuration and model in test script 
    -> test data is edited separatedly in CSV file


'''

singleUser = setUser('user@email.com')
multipleTestData = multipleUsers()

#Set up object to act as 'Server' to retrieve and input data
@pytest.fixture()
def server():
    server = mockServerData('getAllUserGroup')
    return server

#Easier to check individual key and values
@pytest.mark.parametrize("serverData, checkData", [('name', singleUser.name), ('userID', singleUser.userID), ('email', singleUser.email),
('phone', singleUser.phone), ('birthday', singleUser.birthdate), ('gender', singleUser.gender), ('address', singleUser.address), ('group', singleUser.group)])
def test_checkInfo(server, serverData, checkData):
    assert_that(server.serverData[singleUser.index].get(serverData)).is_equal_to(checkData)

#Also possible to add in multiple users 
@pytest.mark.parametrize('testUser', multipleTestData)
@pytest.mark.parametrize("dataType", ['name', 'userID', 'email', 'phone', 'birthday', 'gender', 'address', 'group'])
def test_checkAllUsers(server, testUser, dataType):
    assert_that(server.serverData[testUser.index].get(dataType)).is_equal_to(testUser.json[dataType])

'''
Use this as example, change [group] to [team]
Touch points: 
    1. Test case's parameter
    2. Data configuration
    3. Model
    4. CSV file --> Easy to find and ensure every test data is changed   
--> Harder to demostrate the difference in this sharing session, but for test projects with many test cases or many test data, the difference will be more obvious 
'''

#Show difference in code length adding 5 users
def test_addUser(server):
    num_users = len(server.serverData)
    for user in multipleTestData:
        server.serverData.append(user)
        num_users += 1
    assert_that(len(server.serverData)).is_equal_to(num_users)