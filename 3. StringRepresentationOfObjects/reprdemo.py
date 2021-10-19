from types import ClassMethodDescriptorType


class Positions:
    def __init__(self,latitude,longitude):
        if not (-90 <- latitude <= 90):
            raise ValueError(f"Latitude : {latitude} is out of range")
        if not (-180 <- longitude <= 180):
            raise ValueError(f"Latitude : {latitude} is out of range")
        
        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude
    
    @property
    def longitude(self):
        return self._longitude

    # def __repr__(self):
        # return f"Position {self.latitude} {self.longitude}"
    
    ## Formatting repr as a constructor ##
    # def __repr__(self):
    #     return f"Positions (latitude = {self.latitude}, longitude = {self.longitude})"

    ## Above representation is good but if we want to make subclasses by inheriting this
    ## Then you will need to make the class name dynamic

    def __repr__(self):
        return f"{typename(self)} (latitude = {self.latitude}, longitude = {self.longitude})"


class EarthPosition(Positions):
    pass
class MarsPosition(Positions):
    pass

def typename(obj):
    return type(obj).__name__




oslo = Positions(75,10)
# print(oslo)
# print(repr(oslo))
# print(str(oslo))
# print(format(oslo))

sydney = Positions(87,121)
# print(repr(sydney))
# print(sydney)
# print(type(repr(sydney)))
# print(type(sydney))

## Formatting repr as a constructor ##
#p is a new position object
r = repr(sydney)
p = eval(r) #eval - Evaluated and creates a distinct object from sydney
print(p)
print(p.latitude)

## Demonstrating Inheritance using repr ##
mount_abc = EarthPosition(19.599,99.81)
print(mount_abc)
print(str(mount_abc)) #Both str and format are updated accordingly to __repr__ overriding implementation
print(format(mount_abc))