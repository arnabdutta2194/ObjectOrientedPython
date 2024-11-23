from math import cos,sin

#-- In previous implementation we have seperate Point and PointFactory
#-- If we want to initialize everything in one class, we can use a sub class

class Point:
    def __init__(self,x=0,y=0) :
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f'x : {self.x}, y: {self.y}'

    class PointFactory:
    
        def polar_point(self,x,y): #--- Here factory methods are no longer static methods
            p = Point()
            p.x = x
            p.y = y

            return p

        def cartesian_point(self,rho,theta): 
            return Point(rho * cos(theta), rho * sin(theta))
    factory = PointFactory() #--- Instead of calling point factory directly, we can use something like this
    


p = Point.factory.polar_point(5,6)
p1 = Point.factory.cartesian_point(5,6)

print(p,p1)