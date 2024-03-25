from lib import InputTest


with InputTest(0) as nn:
    nn += int(input())

print(nn)
