class Complex:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __abs__(self):
        self.__x = abs(self.__x)
        self.__y = abs(self.__y)

    def __str__(self):
        return f'{self.__x} + {self.__y}i'

    def __add__(self, other):
        if isinstance(other, Complex):
            x = self.__x + other.__x
            y = self.__y + other.__y
            return Complex(x, y)

        elif isinstance(other, str):
            if other[-1] == 'i':
                y = self.__y + int(other.split('i')[0])
                return Complex(self.__x, y)
            else:
                x = self.__x + int(other)
                return Complex(x, self.__y)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other
