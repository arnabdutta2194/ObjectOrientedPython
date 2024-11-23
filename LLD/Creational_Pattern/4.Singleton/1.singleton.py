
#--- Basic Singleton Class
from typing import Any


class Database:
    _instance = None

    def __new__(cls,*args, **kwargs):
        if not cls._instance: #---Here , when the object is created for the first time, it checks if an instance of the class already existis
            print("Initial object creation")
            cls._instance = super(Database,cls).__new__(cls,*args,**kwargs) #--- If instance of the class does not exist, it creates a new instance, otherwise returns the same instance
        return cls._instance
    def __init__(self):
        print('Loading a Database')
    
d1 = Database()
d2 = Database()
print(d1==d2)      
#--- Problem with above implementation is that the init method gets called everytime an instance of the class is created        


#--- Singleton using decorator

def singleton(class_):
    instances = {}
    def get_instance(*args,**kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args,**kwargs)
        return instances[class_]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print('Loading Database')

print('-------')
d1 = Database()
d2 = Database()


#--- As an alternative to use a singleton implementation as a Decorator, we can implement Singleton as a Metaclass

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]
    
class Database(metaclass = Singleton):
    def __init__(self):
        print('Loading Database')

print('------')
d1 = Database()
d2 = Database()
