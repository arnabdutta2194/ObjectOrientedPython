class GraphicObject:
    def __init__(self,color=None):
        self.color = color
        self.children = []
        self._name = 'Group'
    
    @property
    def name(self):
        return self._name
    
    def _print(self,items,depth):
        items.append('*'*depth)
        if self.color: 
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items,depth+1)    

    def __str__(self) -> str:
        items = []
        self._print(items,0)
        return ''.join(items)

class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'
    
class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'

drawing = GraphicObject()
drawing._name = 'My Drawing'
drawing.children.append(Square('Red'))
drawing.children.append(Circle('Yellow'))

#-- Composite object
group = GraphicObject()
group.children.append(Circle('Yellow'))
group.children.append(Square('Black'))

drawing.children.append(group)

print(drawing)