class Car:
    numberofWheel = 4
    _color = 'Black'
    __yearOfManufacture = 2017

class BMW(Car):
    def __init__(self) -> None:
        print("Color of your BMW is :",self._color)

car = Car()
print(car.numberofWheel)
print(car._color) #--- ACCESSIBLE BUT IS NOT ADVISABLE TO ACCESS
# print(car.__yearOfManufacture) #--- IS NOT ACCESSIBLE
print(car._Car__yearOfManufacture) #--- Way to access Protected Attribute

bmw = BMW()