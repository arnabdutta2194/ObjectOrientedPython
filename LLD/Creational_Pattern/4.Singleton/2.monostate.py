#---- Monostate is a variation of Singleton where we put all the state of an object in a static variable, but at the same time we allow creation of new objects

class CEO:
    __shared_state = {
        'name' : 'Steve',
        'age' : 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state #--- Copying the
    
    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'


ceo1 = CEO()
print(ceo1)

ceo2 = CEO()
ceo2.age = 77
print(ceo1)
print(ceo2)


#--- Monostate class which acts as a super class to a Singleton Class
class Monostate: 
    _shared_state = {}

    def __new__(cls,*args,**kwargs):
        obj = super(Monostate,cls).__new__(cls,*args,**kwargs)
        obj.__dict__ = cls._shared_state
        return obj

class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0
    def __str__(self) -> str:
        return f'{self.name} manages ${self.money_managed}'
    
cfo = CFO()
cfo.name = 'AD'
cfo.money_managed = 200
print('******')
print(cfo)

cfo2 = CFO()
cfo2.name = 'ZZ'
cfo2.money_managed = 300

print('******')
print(cfo)
print(cfo2)