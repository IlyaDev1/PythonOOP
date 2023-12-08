class Complex:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __abs__(self):
        self.__x = abs(self.__x)
        self.__y = abs(self.__y)

    def __str__(self):
        return f'{self.__x} + {self.__y}i'
