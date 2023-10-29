class Coor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Point:
    x = Coor()
    y = Coor()
    z = Coor()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
