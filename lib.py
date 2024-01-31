def _f(s, count, ans):
    result = []
    if count == 0:
        result.append(ans)
        return result

    for c in s:
        result.extend(_f(s, count - 1, ans + c))
    return result


class Product:
    def __init__(self, s, repeat=1):
        self.__mas = _f(s, repeat, '')
        self.__iterIndex = 0

    def __str__(self):
        ans = ''
        for el in self.__mas:
            ans += f'({el}) '
        return ans

    def __iter__(self):
        self.__iterIndex = -1
        return self

    def __next__(self):
        self.__iterIndex += 1
        if self.__iterIndex < len(self.__mas):
            return self.__mas[self.__iterIndex]
        else:
            raise StopIteration

    def __getitem__(self, item):
        return self.__mas[item]

    def __setitem__(self, key, value):
        raise Exception('no')
