class SimpleList:
    def __init__(self,items):
        self._items = list(items)
    def add(self,item):
        self._items.append(item)
    def __getitem__(self,index):
        return self._items[index]
    def sort(self):
        self._items.sort() 
    def __repr__(self):
        return f'{type(self).__name__}({self._items!r})'

class SortedList(SimpleList):
    def __init__(self, items):
        super().__init__(items)
    def add(self, item):
        super().add(item)
        self.sort()

class IntList(SimpleList):
    def __init__(self, items):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x,int):
            raise TypeError('IntList Only Supports Integer')

    def add(self, item):
        self._validate(item)
        return super().add(item)

''' Multiple Inheritance refers to the creation of a class
with more than one Base Class '''

''' Basic Example '''

class Base1:
    def __init__(self):
        print("Base1.__init__")
class Base2:
    def __init__(self):
        print("Base2.__init__")

''' Here Class Sub inherits from Base1 and Base2'''
class Sub(Base1,Base2):
    pass
'''Prints Base1.__init__ as Base1 is first in Method 
Resolution Order '''
s = Sub()


''' Check and Understand MRO '''
print(Sub.__mro__)

'''[Note: Object is the ultimate Base Class for all classes
class Base1 is actually class Base1(object) but we don't
mention it explicitly '''

class SortedIntList(IntList,SortedList):
    pass

print(SortedIntList.__mro__)

s1 = SortedIntList([10,21,2,34,1])
print(s1._items)
''' Python will search through MRO and implement the add
function whereever it finds it first '''
s1.add(10)
print(s1._items)
s1.add("A") #Will throw an error
