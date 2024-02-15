class Frac:
    def __init__(self, *args):
        if len(args) == 2:
            self.__num = args[0]
            self.__denom = args[1]

        elif len(args) == 1:
            obj = args[0]
            if isinstance(obj, str):
                obj = obj.split('/')
                if len(obj) != 2:
                    raise ValueError('not correct str argument')
                self.__num = int(obj[0])
                self.__denom = int(obj[1])

            elif isinstance(obj, int):
                self.__num = obj
                self.__denom = obj

            elif isinstance(obj, float):
                obj = str(obj).split('.')
                self.__num = int(obj[0]) * (10 ** len(obj[1])) + int(obj[1])
                self.__denom = 10 ** len(obj[1])

        else:
            raise TypeError('not correct object type')

    def __str__(self):
        border = ''
        line = '-' * max(len(str(self.__num)), len(str(self.__denom)))
        number = f'           {self.__num}\n' \
                 f'number =   {line}\n' \
                 f'           {self.__denom}'
        border = '-' * len(number)
        number = border + '\n' + number + '\n' + border
        return number

    def __euclid(self, a, b):  # поиск общего знаменателя
        a, b = min(a, b), max(a, b)
        ans = b
        while True:
            if ans % a == 0 and ans % b == 0:
                return ans
            ans += b

    def __com(self, n1, n2):  # поиск новых чисел с общим знаменателем
        com = self.__euclid(n1.__denom, n2.__denom)
        k1 = n1.__num * (com // n1.__denom)
        k2 = n2.__num * (com // n2.__denom)
        return Frac(k1, com), Frac(k2, com)

    def __abs__(self):
        return Frac(abs(self.__num), abs(self.__denom))

    def __add__(self, other):
        if isinstance(other, Frac):
            comRes = self.__com(self, other)
            f1 = comRes[0]
            f2 = comRes[1]
            return Frac(f1.__num + f2.__num, f1.__denom)
        else:
            raise TypeError('only Frac object')

    def __eq__(self, other):
        if isinstance(other, Frac):
            comRes = self.__com(self, other)
            f1 = comRes[0]
            f2 = comRes[1]
            return f1.__num == f2.__num
        else:
            raise TypeError('only Frac object')
