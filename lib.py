class Point:
    __x = 0
    __y = 0
    __MinCoor = 0
    __MaxCoor = 10

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        print(self)

    def getCoor(self):
        return self.__x, self.__y

    def setCoor(self, x, y):
        self.__x = x
        self.__y = y

    def __del__(self):
        print(self)
