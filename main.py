from lib import Frac


a = Frac(2, 5)
b = Frac(20)
c = Frac('20/40')
d = Frac(12.5)
print(a)
print(b)
print(c)
print(d)

e = Frac(-4, 5)
print(abs(e))

print(a + b)

a = Frac(10, 20)
b = Frac(10, 20)
print(a == b, a == e)
