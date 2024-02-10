class BankAccount:
    def __init__(self, login, pwd, cash=0):
        self._login = login
        self._pwd = pwd
        self._cash = cash

    def __str__(self):
        return f'Сумма на счете {self._login}: {self._cash}'

    def __add__(self, other):
        return BankAccount(self._login, self._pwd, self._cash + other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        return BankAccount(self._login, self._pwd, self._cash - other)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        return self - other


class SavingAccount(BankAccount):
    def chargePercent(self):
        self._cash = (self._cash * 1.07 - self._cash) / 12 + self._cash