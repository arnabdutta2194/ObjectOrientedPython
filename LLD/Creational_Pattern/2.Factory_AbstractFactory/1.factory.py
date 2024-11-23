from math import cos, sin


class Point:
    def __init__(self,x,y) :
        self.x = x
        self.y = y

    #--- If the object initialization was not broken down and outsourced to methods, then we would have to write much complex and if loops to do different types of object creation
    @staticmethod  #--- Better naming than init and explanatory
    def polar_point(x,y):
        return Point(x,y)
    
    @staticmethod
    def cartesian_point(rho,theta): #--- Better naming than init and explanatory
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self) -> str:
        return f'x : {self.x}, y: {self.y}'
p = Point(2,3)
p1 = p.cartesian_point(3,4)

print(p,p1)