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
        self._celsius = celcius
    
    @staticmethod
    def _generateCueCard(grade,category="U"):
        cueCardId = ShippingContainer.cueCard + grade + category
        return cueCardId

newOwner7 = GradeBasedShippingContainer.create_with_items("CYZ1235",{"food","textiles","minerals"},celcius=5.0)

print(newOwner7.celsius)
print(newOwner7.contents)
print(newOwner7.cueCardIdNo)