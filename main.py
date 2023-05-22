from lib import Chess


a = Chess(1, 2)
del a.x
print(a.__dict__)


