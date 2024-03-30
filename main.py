from lib import TxtFile


a = TxtFile('test.txt')
print(a.content)
a.addString('hello world')
print(a.content)
