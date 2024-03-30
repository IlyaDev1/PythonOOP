class File:
    def __init__(self, name):
        self._name = name
        self._file = open(self._name, 'a+')

    def __del__(self):
        self._file.close()


class TxtFile(File):
    def __init__(self, name):
        if name[name.rfind('.')+1::] == 'txt':
            if name.count('.') == 1:
                super().__init__(name)
            else:
                raise ValueError('not correct file name')
        self.content = self.getContent(self._file)
        self.__ban = '0123456789'

    @classmethod
    def getContent(cls, file):
        file.seek(0)
        s = file.readlines()
        mas = [el[:-1] for el in s]
        mas[-1] += s[-1][-1]
        return mas

    def addString(self, s):
        for c in self.__ban:
            if c in s:
                raise ValueError('not correct symbol in string')
        self._file.write('\n'+s)
        self.content.append(s)
