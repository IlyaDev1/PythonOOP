class Team:
    def __init__(self, name, *args):
        self.__name = name
        self.__list = list(args)

    def __len__(self):
        return len(self.__list)

    def __str__(self):
        s = f'Name: {self.__name}\n'
        for el in self.__list:
            s += f'\t{el}\n'
        return s
