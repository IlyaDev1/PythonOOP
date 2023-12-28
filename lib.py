class Group:
    def __init__(self, name, persons):
        self.__name = name
        self.__persons = persons

    def __str__(self):
        s = ''
        for el in self.__persons:
            s += f'{el} '
        return s

    def __getitem__(self, item):
        return self.__persons[item]

    def __setitem__(self, key, value):
        self.__persons[key] = value
