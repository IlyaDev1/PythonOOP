from math import sqrt


class Point:
    __x = 0
    __y = 0
    __MinCoor = 0
    __MaxCoor = 10

    @classmethod
    def test(cls, num):
        return cls.__MinCoor <= num <= cls.__MaxCoor

    def __init__(self, x=0, y=0):
        if self.test(x) and self.test(y):
            self.__x = x
            self.__y = y
            print(self)
        else:
            raise(Exception('x, y range'))

    @property
    def CoorX(self):
        return self.__x

    @CoorX.setter
    def CoorX(self, x):
        self.__x = x

    @property
    def CoorY(self):
        return self.__y

    @CoorY.setter
    def CoorY(self, y):
        self.__y = y

    @staticmethod
    def gip(x, y):
        return sqrt(x ** 2 + y ** 2)

    def __del__(self):
        print(self)
