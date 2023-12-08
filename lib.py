class Info:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'эта инфа тебе не нужна'

    def __repr__(self):
        return f'{self.__class__}: {self.__name}'
