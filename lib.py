class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))
