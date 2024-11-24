from abc import ABC

class Renderer(ABC): #--- Abstract Class which will work as Bridge
    def render_circle(self,radius):
        pass
    
    #--Render Square

class VectorRenderer(Renderer):  #--- Abstract Class which will work as Bridge
    def render_circle(self, radius):
        print(f'Drawing a circle of radius : {radius}')

class RasterRenderer(Renderer):  #--- Abstract Class which will work as Bridge
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')

class Shape:
    def __init__(self,renderer): #--- Conecting interface to implementation
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self):
        pass

class Circle(Shape):
    def __init__(self, renderer,radius):
        super().__init__(renderer)
        self.radius = radius
    
    def draw(self): #--- Here we will need to use the bridge
        self.renderer.render_circle(self.radius)
    
    def resize(self,factor):
        self.radius *= factor

raster_renderer = RasterRenderer()
vector_renderer = VectorRenderer()

circle = Circle(vector_renderer,5)
circle.draw()
circle.resize(5)
circle.draw()


circle = Circle(raster_renderer,5)
circle.draw()
circle.resize(5)
circle.draw()


#--- The prblem with the above implementation is that if we now have to use a triangle, we will need to create a render_triangle method which breaks the open closed principle

