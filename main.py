from lib import CheckTime


def cube(x):
    return x ** 3


def values(start, end):
    mas = []
    for i in range(start, end+1):
        mas.append(cube(i))
    return mas


time = CheckTime(values)
print(time(-1000000, 1000000))
