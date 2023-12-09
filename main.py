from lib import Complex


n1 = Complex(-2, 3)
n1 = n1 + '5'
n1 = n1 + '6i'
print(n1)
n2 = Complex(10, 10)
n3 = n1 + n2
print(n3)
n4 = '100' + n3
print(n4)
nx = Complex(1, 2)
ny = Complex(3, 4)
nx += ny
print(nx)
