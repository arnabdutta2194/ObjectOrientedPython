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
    def initialize_container(cls,owner_code):  #Named Constructors
        return cls(owner_code,contents = [])

    @classmethod
    def create_with_items(cls,owner_code,items):  #Named Constructors
        return cls(owner_code,contents = list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()
        self.cueCardIdNo = ShippingContainer._generateCueCard("X")
newOwner3 = ShippingContainer.initialize_container("XYZ1234") #named constructor
newOwner4 = ShippingContainer.create_with_items("XYZ1235",{"food","textiles","minerals"}) #named constructor

print(newOwner3.owner_code)
print(newOwner3.contents)
print(newOwner3.serial)

print(newOwner4.owner_code)
print(newOwner4.contents)
print(newOwner4.serial)
print(newOwner4.cueCardIdNo)