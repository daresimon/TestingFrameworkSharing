class mockServerData:

    def __init__(self, purpose):
        self.serverData = []
        self.addPermission = 'yes'
        if purpose == 'getUser':
            self.serverData.append(self.userData())
        elif purpose == 'getAllUserGroup':
            self.allUserGroup()
        elif purpose == 'getAllUserTeam':
            self.allUserTeam()
        else:
            pass
        
    def userData(self):
        user_data = {
            'name': 'userName',
            'userID': 123,
            'email': 'user@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        }
        return user_data

    def allUserGroup(self):
        user_data = {
            'name': 'userName',
            'userID': 123,
            'email': 'user@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        }
        user_data2 = {
            'name': 'userName2',
            'userID': 123,
            'email': 'user2@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        }
        user_data3 = {
            'name': 'userName3',
            'userID': 123,
            'email': 'user3@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        }
        user_data4 = {
            'name': 'userName4',
            'userID': 123,
            'email': 'user4@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        }
        user_data5 = {
            'name': 'userName5',
            'userID': 123,
            'email': 'user5@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'group': 'Group A'
        }
        self.serverData.append(user_data)
        self.serverData.append(user_data2)
        self.serverData.append(user_data3)
        self.serverData.append(user_data4)
        self.serverData.append(user_data5)


    def allUserTeam(self):
        user_data = {
            'name': 'userName',
            'userID': 123,
            'email': 'user@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'team': 'Team A'
        }
        user_data2 = {
            'name': 'userName2',
            'userID': 123,
            'email': 'user2@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'team': 'Team A'
        }
        user_data3 = {
            'name': 'userName3',
            'userID': 123,
            'email': 'user3@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'team': 'Team A'
        }
        user_data4 = {
            'name': 'userName4',
            'userID': 123,
            'email': 'user4@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'team': 'Team A'
        }
        user_data5 = {
            'name': 'userName5',
            'userID': 123,
            'email': 'user5@email.com',
            'phone': '+65 91234567',
            'birthday': '1990-01-01',
            'gender': 'male',
            'address': 'Blk 123 My Home Street 3 Singapore 123456',
            'team': 'Team A'
        }
        self.serverData.append(user_data)
        self.serverData.append(user_data2)
        self.serverData.append(user_data3)
        self.serverData.append(user_data4)
        self.serverData.append(user_data5)
                    
