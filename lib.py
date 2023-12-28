from math import sqrt


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __radiusVector(self):
        return sqrt(self.__x ** 2 + self.__y ** 2)

    def __len__(self):
        return int(self.__radiusVector())

    def __bool__(self):
        if len(self) != 0: return True
        return False
