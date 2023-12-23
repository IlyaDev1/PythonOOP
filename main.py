from lib import Complex


c1 = Complex(-2, -5)
c2 = Complex(5, 10)

c3 = c1 + c2
c4 = 5 + c2 + 6
c2 += c1
print(c1, c2, c3, c4, sep='\n')
