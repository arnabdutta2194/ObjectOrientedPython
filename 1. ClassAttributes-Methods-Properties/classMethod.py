class ShippingContainer:
    next_Serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_Serial
        cls.next_Serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

newOwner1 = ShippingContainer("XYZ123",["books","boxes"])
newOwner2 = ShippingContainer("XYZ123",["books","boxes"])

print(newOwner1.contents)
print(newOwner1.owner_code)
print(newOwner1.serial)

print(newOwner2.contents)
print(newOwner2.owner_code)
print(newOwner2.serial)

# print(ShippingContainer.next_Serial)