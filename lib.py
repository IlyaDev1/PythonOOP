from datetime import datetime


class CheckTime:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        __start = datetime.now()
        self.__func(*args)
        return datetime.now() - __start
