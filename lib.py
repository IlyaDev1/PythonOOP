from os import system


class Account:
    def __init__(self, name):
        self.__name = name
        self.__cash = 0

    def __str__(self):
        s = f'Счет: {self.__name} | Средства: {self.__cash}[RUB]'
        return s

    def __setattr__(self, key, value):
        if key == '_Account___cash':
            if value < 0:
                raise ValueError('not enough money in the account')
        object.__setattr__(self, key, value)

    def __testStream(self, value):
        if value < 0:
            raise ValueError('only positive value')

    def add(self, value):
        self.__testStream(value)
        self.__cash += value

    def take(self, value):
        self.__testStream(value)
        self.__cash -= value


class Brokerage(Account):
    def __init__(self, name):
        super().__init__(name)
        self.__cur = {}
        self.__assets = {}

    @staticmethod
    def openCurrency():
        system('notepad Currency.txt')

    @staticmethod
    def openStock():
        system('notepad Stock.txt')

    def __str__(self):
        s = super().__str__()
        s += f' | {self.__cur} | {self.__assets}'
        return s

    def __findCurrency(self, name):
        with open('Currency.txt') as file:
            fileString = file.readline()
            while fileString != '':
                CurrencyList = fileString.split(': ')
                if CurrencyList[0] == name:
                    return int(CurrencyList[1][:-1])
        raise Exception('not correct asset name')

    def buyCurrency(self, name, amount):
        cost = self.__findCurrency(name) * amount
        super().take(cost)
        try:
            self.__cur[name] += amount
        except KeyError:
            self.__cur[name] = 0
        finally:
            self.__cur[name] += amount