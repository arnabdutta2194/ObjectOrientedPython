class ShippingContainer:
    next_Serial = 1337
    cueCard = "1234"
    Height_FT = 8.0 #Height and Width are Class attributes as they are always in common
    Width_FT = 7.0

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
    def initialize_container(cls,length_ft,owner_code,**kwargs):
        return cls(owner_code,length_ft,contents = [],grade="X",**kwargs)

    @classmethod
    def create_with_items(cls,owner_code,length_ft,items,**kwargs):
        return cls(owner_code,length_ft,contents = list(items),grade="X",**kwargs)

    def __init__(self, owner_code, length_ft,contents,grade,**kwargs): ##Length_ft is instance attribute so it is part of initializer
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
        self.cueCardIdNo = self._generateCueCard(grade)

    @property
    def volume_ft3(self):
        return ShippingContainer.Height_FT * ShippingContainer.Width_FT * self.length_ft

#---------- Sub Class ----------#
class GradeBasedShippingContainer(ShippingContainer):

    ##Method Overriding 
    MAX_CELCIUS = 4.0
    FridgeVolume = 20

    def __init__(self, owner_code, length_ft,contents, grade, *,celcius,**kwargs):
        super().__init__(owner_code, length_ft, contents, grade,**kwargs)
        if celcius > GradeBasedShippingContainer.MAX_CELCIUS:
            raise ValueError("Temperature Too Hot")
        self.celcius = celcius #Assign to property rather than assigning to the attribute

    @staticmethod
    def volume_ft3(self):
        return ( super().volume_ft3 - GradeBasedShippingContainer.FridgeVolume)
    
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

newOwner7 = GradeBasedShippingContainer.create_with_items("CYZ1235",20,{"food","textiles","minerals"},celcius=-10.0)

print(newOwner7.volume_ft3)