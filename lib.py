from math import sqrt


class Complex:
    def __init__(self, r, i):
        self.__r = r
        self.__i = i

    def __str__(self):
        if self.__i > 0:
            return f'{self.__r} + {self.__i}i'
        else:
            return f'{self.__r} - {abs(self.__i)}i'

    def __abs__(self):
        return Complex(abs(self.__r), abs(self.__i))

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__r + other.__r, self.__i + other.__i)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.__r + other, self.__i)
        else:
            raise TypeError('not correct other data')

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __gipo(self, r, i):
        return sqrt(r*r + i*i)

    def __eq__(self, other):
        fst = self.__gipo(self.__r, self.__i)
        scd = self.__gipo(other.__r, self.__i)
        return fst == scd

    #eq ==, ne !=, lt <, le <=, gt >, ge >=