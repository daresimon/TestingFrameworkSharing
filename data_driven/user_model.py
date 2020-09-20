'''
Set up a model to load test data into an object
-> Advantage over loading data directly into object without model:
    -> For attributes that can be left blank, it will appear in expected data type
    -> For example, if user birthdate is empty, it will be an empty string 
    -> In comparison, if data is loaded directly, it will be [null] since the CSV file will have no input
'''

class user:
    __name = ''
    __userID = ''
    __email = ''
    __phone = ''
    __birthdate = ''
    __gender = ''
    __address = ''
    __group = ''
    __index = ''
    __json = ''

    def __init__(self, index):
        self.__index = index

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, ind):
        self.__index = ind

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, inputName):
        self.__name = inputName

    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, ID):
        self.__userID = ID

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, address):
        self.__email = address

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, number):
        self.__phone = number

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, date):
        self.__birthdate = date

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gen):
        self.__gender = gen

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, add):
        self.__address = add

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, grp):
        self.__group = grp

    @property
    def json(self):
        return self.__json

    @json.setter
    def json(self, js):
        self.__json = js