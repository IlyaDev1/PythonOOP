class TGame:
    __slots__ = ('__mapa')

    def __init__(self):
        self.__mapa = [[None]*3 for i in range(3)]

    def __str__(self):
        s = ''
        for el in self.__mapa:
            s += str(el) + '\n'
        return s

    def setHod(self, posX, posY, value):
        if posX > 2 or posX < 0 or posY > 2 or posY < 0:
            raise MapBorderException('ты вышел за границы карты')


class MapBorderException(IndexError):
    def __init__(self, *args):
        self.__message = args

    def __str__(self):
        return f'ошибка: {self.__message}'