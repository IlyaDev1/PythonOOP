class Point:
    x = 0
    __y = 0
    __MinCoor = 0
    __MaxCoor = 10

    @classmethod
    def testCoor(cls, value):
        return cls.__MinCoor <= value <= cls.__MaxCoor

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        print(f'object was created: {self}')

    def getCoor(self):
        return self.__x, self.__y

    def setCoor(self, x, y):
        self.__x = x
        self.__y = y

    def __getattribute__(self, item):  # вызывается, если мы обращаемся к переменной
        if item == 'x' or item == '__x' or item == 'y' or item == '__y':
            raise Exception('нельзя юзать эту переменную')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # вызывается, если мы редачим переменную
        if key == '_Point__x' or key == '_Point__y':
            if not self.testCoor(value):
                raise Exception('Вы вводите неверные значения')
        object.__setattr__(self, key, value)

    def __getattr__(self, item):  # вызывается при обращении к несущ атр
        return 'вы исп несущ атр'

    def __delattr__(self, item):
        print(f'был удален атр {item}')
        object.__delattr__(self, item)

    def __del__(self):
        print(f'object was deleted: {self}')
