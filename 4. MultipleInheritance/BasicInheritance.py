### ---- Example 1 ---- ###

class Base:
    def __init__(self):
        print("Base Class Initializer")

    def f(self):
        print("Base.f()")

class Sub(Base):
    def __init__(self):
        super().__init__()
        print("Sub Class Initializer")

    
    def f(self):
        print("Sub.f()")

a = Sub()

### ---- Example 2 ---- ###

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

s1 = SortedList([55,8,98,9,32])
s1.add(72)
print(s1._items)
print(s1.__getitem__(2))
print(repr(s1))

print(isinstance(s1,SortedList))
print(isinstance(s1,SimpleList))

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

s2 = IntList([55,8,98,9,32])
# print(s1._items)
s2.add(4)
print(s2._items)
# s1.add("A")

print(issubclass(IntList,SimpleList))