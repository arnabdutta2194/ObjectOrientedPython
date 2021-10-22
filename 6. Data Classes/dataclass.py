from position import Positions,EarthPosition
from position import typename
from dataclasses import dataclass


'''Decorate your class with Data Class Decorator'''
@dataclass 
class Location:
    name : str
    position : Positions


hongkong = Location("Hong Kong",Positions(22.29,114.16))
print(hongkong.__repr__())