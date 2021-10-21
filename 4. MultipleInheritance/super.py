class Animal:
    @classmethod
    def description(cls):
        return "An Animal"

class Bird(Animal):
    @classmethod
    def description(cls):
        s = super() 
        print(s) #Printing the Super Proxy
        ''' The above Super Proxy (s) results in <super: <class 'Bird'>, <Flamingo object>>
        So it means it searches in the Mro after Bird'''
        return super().description() + " With Wings"

class Flamingo(Bird):
    @classmethod
    def description(cls):
        return super().description() + " and fabulous pink feathers"


s = Flamingo()
print(s.description())