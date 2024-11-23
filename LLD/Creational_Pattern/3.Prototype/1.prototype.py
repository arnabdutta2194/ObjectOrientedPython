import copy

class Address:
    def __init__(self,city,street_address,country):
        self.city = city
        self.street_address =street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address,self.city,self.country}'


class Person:
    def __init__(self,name,address):
        self.name = name
        self.address =address

    def __str__(self):
        return f'{self.name} lives in {self.address}'

john = Person('John',Address('London','12 becker Street','UK'))
print(john)
ad = john #--- Both ad and john refers to the same object so this is not exactly a copy
ad.name = 'AD'
ad.address.street_address = '123 B London road' #-- Both ad and john refers to the same address object
print('******')
print(ad)
print(john)
#--- In the above implementation, john and ad now both refer to the same object

#--- In order to resolve the abovem we can do something like copy.deepcopy() which recursively copies everything as if both objects are similar

john = Person('John',Address('London','12 becker Street','UK'))
ad = copy.deepcopy(john)
ad.name = 'AD'
ad.address.street_address = '123 B London Road'
print('******')
print(ad)
print(john)