
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

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >=0 else "S"
    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >=0 else "W"


    def __repr__(self):
        return f"{typename(self)} (latitude = {self.latitude}, longitude = {self.longitude})"

    def __str__(self):
        return (f"{abs(self.latitude)} degree {self.latitude_hemisphere},"
         f"{abs(self.longitude)} degree {self.longitude_hemisphere}")

    def __format__(self, format_spec):
        latitude = format(abs(self.latitude),".1f")
        longitude = format(abs(self.longitude),".1f")
        return (f"{latitude} degree {self.latitude_hemisphere},"
         f"{longitude} degree {self.longitude_hemisphere}")

class EarthPosition(Positions):
    pass
class MarsPosition(Positions):
    pass

def typename(obj):
    return type(obj).__name__

mountErebros = EarthPosition(-77.5,167.2)
print(format(mountErebros))
print(f"The mountain of Antartica is {mountErebros}")