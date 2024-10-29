class ShippingContainer:
    next_Serial = 1337
    cueCard = "1234"

    @classmethod
    def _generate_serial(cls):
        result = cls.next_Serial
        cls.next_Serial += 1
        return result

    @staticmethod
    def _generateCueCard(grade,category="Z"):
        cueCardId = ShippingContainer.cueCard + grade + category
        return cueCardId


    @classmethod
    def initialize_container(cls,owner_code,**kwargs):
        return cls(owner_code,contents = [],**kwargs)

    @classmethod
    def create_with_items(cls,owner_code,items,**kwargs):
        print(kwargs)
        return cls(owner_code,contents = list(items),grade="X",**kwargs)

    def __init__(self, owner_code, contents,grade,**kwargs):
        print("Inside init")
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
        self.cueCardIdNo = self._generateCueCard(grade)

newOwner4 = ShippingContainer("XYZ1235",{"food","textiles","minerals"},"A")


class GradeBasedShippingContainer(ShippingContainer):

    ##Method Overriding 
    MAX_CELCIUS = 4.0

    def __init__(self, owner_code, contents, grade, *,celcius,**kwargs):
        super().__init__(owner_code, contents, grade,**kwargs)
        if celcius > GradeBasedShippingContainer.MAX_CELCIUS:
            raise ValueError("Temperature Too Hot")
        self.celcius = celcius #Assign to property rather than assigning to the attribute

    @property #When we decorate celcius method with property the returned object is also bound to the name celcius
    def celcius(self): #Getter Method
        return self._celcius

    @celcius.setter
    def celcius(self,value): #Setter Method
        if value > GradeBasedShippingContainer.MAX_CELCIUS:
            raise ValueError("Temperature Too Hot")
        self._celcius = value

    @staticmethod
    def _generateCueCard(grade,category="U"):
        cueCardId = ShippingContainer.cueCard + grade + category
        return cueCardId

newOwner7 = GradeBasedShippingContainer.create_with_items("CYZ1235",{"food","textiles","minerals"},celcius=-10.0)

print(newOwner7.contents)
print(newOwner7.cueCardIdNo)
print(newOwner7.celcius) #Here Celcius is a property used as a variable
newOwner7.celcius=-19
print(newOwner7.celcius)