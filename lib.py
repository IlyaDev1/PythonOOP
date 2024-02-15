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

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__r - other.__r, self.__i - other.__i)
        elif isinstance(other, int) or isinstance(other, float):
            return Complex(self.__r - other, self.__i)
        else:
            raise TypeError('not correct other data')

    def __isub__(self, other):
        return self - other

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        if type(other) in [int, float]:  # здесь представлена более "красивая" запись
            other = Complex(other, 0)
        if isinstance(other, Complex):
            r = self.__r*other.__r - self.__i*other.__i
            i = self.__r*other.__i + self.__i*other.__r
            return Complex(r, i)
        else:
            raise TypeError('not correct other data')

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) in [int, float]:
            other = Complex(other, 0)
        if isinstance(other, Complex):
            r = (self.__r*other.__r + self.__i*other.__i) / (other.__r**2+other.__i**2)
            i = (other.__r*self.__i - self.__r*other.__i) / (other.__r**2+other.__i**2)
            return Complex(r, i)
        else:
            raise TypeError('not correct other data')

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        return self / other
