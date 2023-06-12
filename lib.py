class User:
    __name = ''
    __id = 0
    __balance = 0

    def __init__(self, object=None):
        if object is None:
            self.__id = 0
        else:
            self.__id = object.__id + 1
        self.__name = f'User{self.__id}'

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance
