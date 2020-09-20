import pytest
from data_driven.mockServer import mockServerData
from assertpy import assert_that

'''
Easy to setup as everything is just coded according to requirements
-> Eg to check a user's data, just enter the expected data and enter statement to check data

4 examples to demostrate pros and cons:
-> Straightforward test case setup
-> Code repetitiveness due to hard coding data
-> Lengthy code due to data size
-> Inconvenience when changing data
'''

#Set up object to act as 'Server' to retrieve and input data
@pytest.fixture()
def server():
    server = mockServerData('getUser')
    return server

#To describe convenience and easy to setup linear script
def test_checkUser(server):
    check_user_data = {
        'name': 'userName',
        'userID': 123,
        'email': 'user@email.com',
        'phone': '+65 91234567',
        'birthday': '1990-01-01',
        'gender': 'male',
        'address': 'Blk 123 My Home Street 3 Singapore 123456',
        'group': 'Group A'
    }
    assert_that(check_user_data).is_equal_to(server.serverData[0])

#To show repetitiveness
def test_checkUserName(server):
    check_user_data = {
        'name': 'userName',
        'userID': 123,
        'email': 'user@email.com',
        'phone': '+65 91234567',
        'birthday': '1990-01-01',
        'gender': 'male',
        'address': 'Blk 123 My Home Street 3 Singapore 123456',
        'group': 'Group A'
    }
    assert_that(check_user_data.get('name')).is_equal_to(server.serverData[0].get('name'))

def test_checkUserID(server):
    check_user_data = {
        'name': 'userName',
        'userID': 123,
        'email': 'user@email.com',
        'phone': '+65 91234567',
        'birthday': '1990-01-01',
        'gender': 'male',
        'address': 'Blk 123 My Home Street 3 Singapore 123456',
        'group': 'Group A'
    }
    assert_that(check_user_data.get('userID')).is_equal_to(server.serverData[0].get('userID'))
    
#To show how long the code can get 
def test_add5User(server):
    num_users = len(server.serverData)
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
    add_user_data2 = {
            'name': 'newUser2',
            'userID': 2345,
            'email': 'newUser2@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    server.serverData.append(add_user_data2)
    add_user_data3 = {
            'name': 'newUser3',
            'userID': 2345,
            'email': 'newUser3@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    server.serverData.append(add_user_data3)
    add_user_data4 = {
            'name': 'newUser4',
            'userID': 2345,
            'email': 'newUser4@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    server.serverData.append(add_user_data4)
    add_user_data5 = {
            'name': 'newUser5',
            'userID': 2345,
            'email': 'newUser5@email.com',
            'phone': '+65 90000000',
            'birthday': '1991-01-01',
            'gender': 'male',
            'address': 'Blk 321 My House Street 1 Singapore 234567',
            'group': 'Group A'
        }
    server.serverData.append(add_user_data5)
    assert_that(len(server.serverData)).is_equal_to(num_users + 5)

#To show change in data type (change 'group' to 'team' AND describe mass change in data)
def test_checkAllUserGroup(server):
    testCaseServer = mockServerData('getAllUserGroup')
    testUsers = [
        {
            'name': 'userName',
            'userID': 123,
            'email': 'user@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        },
        {
            'name': 'userName2',
            'userID': 123,
            'email': 'user2@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        },
        {
            'name': 'userName3',
            'userID': 123,
            'email': 'user3@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        },
        {
            'name': 'userName4',
            'userID': 123,
            'email': 'user4@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        },
        {
            'name': 'userName5',
            'userID': 123,
            'email': 'user5@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        }
    ]
    for user, testUser in zip(testCaseServer.serverData, testUsers):
        assert_that(user.get('group')).is_equal_to(testUser.get('group'))

    '''
    If there are multiple scripts that uses the same data, the changes have to be made to multiple scripts as well
        -> Time consuming
        -> High maintenance cost
        -> easy to make mistakes (miss something out)
    '''
