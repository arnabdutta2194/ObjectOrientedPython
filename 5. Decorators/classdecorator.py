from position import EarthPosition
from position import typename
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position
    
    '''For Each input a property is available of the same name and which returns the same type of object'''
    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position

    def __repr__(self):
        return f"{typename(self)}(name = {self.name}, position = {self.position})"

    def __str__(self):
        return self.name
''' Earth Position Will Create a object of the given Latitude and Longitude and will return the __format__ Representation of Position'''
# hongkong = Location("HongKong", EarthPosition(10.50,22.31))
# print(hongkong) #__str__ Version of Location Class
# print(hongkong.position) #Position Which is returned from __format__ method of EarthPosition
# print(hongkong.__repr__()) #__repr__ Version of Location Class

def check_name(method):
    def inner(name_ref):
        if name_ref._name == "Test":
            print("Hey My Name is Also Same")
        else:
            method(name_ref)
    return inner


class Printing:
    def __init__(self,name):
        self._name = name
    @check_name
    def print_name(self):
        print("Entered User Name is : " + self._name)
p = Printing("Test")
p.print_name()
p = Printing("Test")
p.print_name()
