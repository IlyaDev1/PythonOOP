class Counter:
    def __init__(self):
        self.__count = 0

    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__count += 1
        return self.__count
