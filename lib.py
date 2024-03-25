class InputTest:
    def __init__(self, value):
        self.__value = value

    def __enter__(self):
        self.__temp = self.__value
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__value = self.__temp

        return False
