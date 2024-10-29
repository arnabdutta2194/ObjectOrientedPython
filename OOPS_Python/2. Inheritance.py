#-- Python checks attributes in the following order:
# 1. First it checks if it is an instance attribute
# 2. Then it checks if it is a class attribute
# 3. Then it checks if it is an attribute of your BaseClass


#--1. Single Inheritance

class Apple:
    manufacturer = "Apple Inc"
    contactWebsite= "www.apple.com/contact"

    def contactDetails(self):
        print("To Contact Us, log on to", self.contactWebsite)

class MacBook(Apple): #--- Inherited the Base Class Attributes as well as the Base Class Methods
    def __init__(self) -> None:
        self.yearOfManufacture = 2017
    
    def manufactureDetails(self):
        print(f"This macbook was manufactured in the year : {self.yearOfManufacture} by {self.manufacturer}")

macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()

print("**************")


#--2. Multiple Inheritance

class OperatingSystem:
    multiTasking = True
    name = 'MacOS'
    contactWebsite= "www.macos.com/contact"
    manufacturer = "AppleSystems INC"

class Apple:
    manufacturer = "Apple Inc"
    contactWebsite= "www.apple.com/contact"

    def contactDetails(self):
        print("To Contact Us, log on to", self.contactWebsite)

class MacBook(Apple,OperatingSystem): #--- Inherited the Base Class Attributes as well as the Base Class Methods from both the classes
    #-- MRO ---  1. Apple Class 2. OperatingSystem Class
    def __init__(self) -> None:
        self.yearOfManufacture = 2017
        if self.multiTasking:
            print("This is a MultiTasking System")
    
    def manufactureDetails(self):
        print(f"This macbook was manufactured in the year : {self.yearOfManufacture} by {self.manufacturer}")
        #-- here the manufacturer will be printed as Apple Inc and not AppleSystem Inc due to the Method of order resoltuion
    

macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()


#--3. MultiLevel Inheritance
# -- ClassA --> ClassB -->ClassC

class MusicalInstruments:
    numberofMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeofWood = "ToneWood"

class Guitar(StringInstruments):
    def __init__(self) -> None:
        self.numberOfStrings = 6
        print(f"The guitar consists of {self.numberOfStrings} Strings, {self.numberofMajorKeys} Keys and is made up of {self.typeofWood} Wood")
guitar = Guitar()

