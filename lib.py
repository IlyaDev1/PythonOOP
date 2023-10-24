class Worker:  # Класс не доработан, но показывает суть задания
    __passport = ''
    __name = ''
    __payment = 0
    __old = 0
    __MinOld = 16
    __MaxOld = 70

    def __testName__(self, s):  # нужно пояснить, что так можно инкапсулировать методы
        numbers = [str(i) for i in range(0, 10)]
        mas = s.split()
        if len(mas) == 3:
            for i in range(3):
                for j in range(len(numbers)):
                    if numbers[j] in mas[i]:
                        return False
        else:
            return False
        return True

    @classmethod
    def testOld(cls, value):
        return cls.__MinOld <= value <= cls.__MaxOld

    def __init__(self, passport, name, payment, old):
        self.__passport = passport
        self.__name = name
        self.__payment = payment
        self.__old = old

    def __setattr__(self, key, value):
        if key == '_Worker__name':
            if not self.__testName__(value):
                raise Exception('неверно введены данные ФИО')

        if key == '_Worker__old':
            if not self.testOld(value):
                raise Exception('неверно введены данные возраста')

        object.__setattr__(self, key, value)
