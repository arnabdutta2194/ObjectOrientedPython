from math import cos,sin

#--- But previous implementation is still dependent on the initializer
#--- In order to remove dependency from the initializer, we can implement something which is called a factory class


class Point:
    def __init__(self,x=0,y=0) :
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f'x : {self.x}, y: {self.y}'

class PointBulder:
    #--- If the object initialization was not broken down and outsourced to methods, then we would have to write much complex and if loops to do different types of object creation
    @staticmethod  #--- Better naming than init and explanatory
    def polar_point(x,y):
        p = Point(x,y)
        p.x = x
        p.y = y
        return p

    @staticmethod
    def cartesian_point(rho,theta): #--- Better naming than init and explanatory
        return Point(rho * cos(theta), rho * sin(theta))


p = PointBulder.polar_point(2,3)
p1 = PointBulder.cartesian_point(3,4)

print(p,p1)