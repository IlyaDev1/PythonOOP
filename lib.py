class Point:
    __minCoor = 0
    __maxCoor = 1000

    @classmethod
    def test(cls, x, y):
        return cls.__minCoor <= x <= cls.__maxCoor and cls.__minCoor <= y <= cls.__maxCoor

    def __init__(self, x, y):
        if self.test(x, y):
            self.__x = x
            self.__y = y
            print(f'created: {self}')
        else:
            raise Exception('no')

    def getCoor(self):
        return self.__x, self.__y

    def setCoor(self, x, y):
        self.__x = x
        self.__y = y

    def __del__(self):
        print(f'deleted: {self}')

    @staticmethod
    def gip(a, b):
        return (a ** 2 + b ** 2) ** 0.5
