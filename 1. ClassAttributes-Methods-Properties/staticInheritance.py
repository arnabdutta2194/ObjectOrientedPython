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
    def initialize_container(cls,owner_code):
        return cls(owner_code,contents = [])

    @classmethod
    def create_with_items(cls,owner_code,items):
        return cls(owner_code,contents = list(items),grade="X")

    def __init__(self, owner_code, contents,grade):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
        self.cueCardIdNo = self._generateCueCard(grade)

newOwner4 = ShippingContainer("XYZ1235",{"food","textiles","minerals"},"A")


class GradeBasedShippingContainer(ShippingContainer):

    ##Method Overriding 
    MAX_CELCIUS = 4.0

    def __init__(self, owner_code, contents, grade, celcius):
        super().__init__(owner_code, contents, grade)
        if celcius > GradeBasedShippingContainer.MAX_CELCIUS:
            raise ValueError("Temperature Too Hot")
        self.celsius = celcius

    @staticmethod
    def _generateCueCard(grade,category="U"):
        cueCardId = ShippingContainer.cueCard + grade + category
        return cueCardId

newOwner5 = GradeBasedShippingContainer("XYZ1235",{"food","textiles","minerals"},"A")
newOwner6 = GradeBasedShippingContainer.create_with_items("CYZ1235",{"food","textiles","minerals"})
newOwner7 = GradeBasedShippingContainer.create_with_items("CYZ1235",{"food","textiles","minerals"})

# print(newOwner5._generateCueCard("A"))
# print(newOwner4._generateCueCard("A"))

# print(newOwner5.cueCardIdNo)
# print(newOwner4.cueCardIdNo)
# print(newOwner6.owner_code)


