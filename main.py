from lib import Brokerage


a = Brokerage('ilya')
print(a)
a.add(2000)
a.buyCurrency('USD', 2)
print(a)
