from math import sqrt


class Chess:
    __Min = 0
    __Max = 7
    x = 0
    __y = 0

    @classmethod
    def testCoor(cls, value):
        return cls.__Min <= value <= cls.__Max

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getCoor(self):
        return (self.__x, self.__y)

    def setCoor(self, x, y):
        self.__x = x
        self.__y = y

    def __getattribute__(self, item):
        if item == "setCoor":
            print('you are using setCoor')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == '_Chess__x' or key == '_Chess__y':
            if not self.testCoor(value):
                raise Exception('no')
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print('getattr was called')

    def __delattr__(self, item):
        print('delattr was called')

    @staticmethod
    def gip(x, y):
        return sqrt(x ** 2 + y ** 2)
