import pandas as pd
from data_driven.user_model import user

def setUser(email):

    df = pd.read_csv('./data_driven/userData.csv')
    thisUser = df.loc[df["email"] == email]

    currentUser = user(thisUser['index'].values[0])
    currentUser.name = thisUser['name'].values[0]
    currentUser.userID = thisUser['userID'].values[0]
    currentUser.email = thisUser['email'].values[0]
    currentUser.phone = thisUser['phone'].values[0]
    currentUser.birthdate = thisUser['birthdate'].values[0]
    currentUser.gender = thisUser['gender'].values[0]
    currentUser.address = thisUser['address'].values[0]
    currentUser.group = thisUser['group'].values[0]

    return currentUser

def multipleUsers():
    userList = []

    df = pd.read_csv('./data_driven/userData.csv')
    for i, row in df.iterrows():
        rowUser = user(row['index'])
        rowUser.name = row['name']
        rowUser.userID = row['userID']
        rowUser.email = row['email']
        rowUser.phone = row['phone']
        if not pd.isna(row["birthdate"]): #For attributes that could be left empty by user/admin
            rowUser.birthdate = row['birthdate']
        rowUser.gender = row['gender']
        rowUser.address = row['address']
        rowUser.group = row['group']
        rowUser.json = {
            'name': rowUser.name,
            'userID': rowUser.userID,
            'email': rowUser.email,
            'phone': rowUser.phone,
            'birthday': rowUser.birthdate,
            'gender': rowUser.gender,
            'address': rowUser.address,
            'group': rowUser.group
        }
        userList.append(rowUser)
    

    return userList
