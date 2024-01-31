class Elem:
    def __init__(self, value=None, nextElem=None):
        self.value = value
        self.nextElem = nextElem


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        currentElem = Elem(value, self.head)
        while currentElem.nextElem != None:
            currentElem = currentElem.nextElem
        newElem = Elem(value, None)
        currentElem.nextElem = newElem
        if self.head is None: self.head = currentElem

    def print(self):
        currentElem = self.head
        while currentElem.nextElem != None:
            currentElem = currentElem.nextElem
            print(currentElem.value, end=', ')
