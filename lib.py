class Point2D:
    __slots__ = ('_x', '_y')

    def __init__(self, x, y):
        self._x = x
        self._y = y


class Point3D(Point2D):
    __slots__ = ('__z')

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def __str__(self):
        return f'{self._x}, {self._y}, {self.__z}'