class ShippingContainer:
    next_Serial = 1337
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # self.serial = ShippingContainer.next_Serial
        ### --- Best Practice ---###
        self.serial = self.next_Serial
        # self.next_Serial += 1
        ShippingContainer.next_Serial +=1


newOwner1 = ShippingContainer("XYZ123",["books","boxes"])
newOwner2 = ShippingContainer("XYZ123",["books","boxes"])

print(newOwner1.contents)
print(newOwner1.owner_code)
print(newOwner1.serial)

print(newOwner2.contents)
print(newOwner2.owner_code)
print(newOwner2.serial)

# print(ShippingContainer.next_Serial)