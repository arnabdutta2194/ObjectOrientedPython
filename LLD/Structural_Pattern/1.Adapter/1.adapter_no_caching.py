from typing import Iterable


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def draw_point(p):
    print('.',end='')

class Line:
    def __init__(self,start,end):
        self.start = start
        self.end = end

class Rectangle(list):
    def __init__(self,x,y,height,width):
        super().__init__()
        self.append(Line(Point(x,y),Point(x+width,y)))
        self.append(Line(Point(x+width,y),Point(x+height,y+width)))
        self.append(Line(Point(x,y),Point(x,y+height)))
        self.append(Line(Point(x,y+height),Point(x+width,y+height)))

#--- We need to build an adapter which will have all the points in a line
class LineToPointAdapter(list):
    count = 0
    def __init__(self,line):
        super().__init__()
        self.count +=1

        print(f'{self.count} : Generating points for a line '
              f'[{line.start.x},{line.start.y}] ->'
              f'[{line.end.x},{line.end.y}] ->')
        left = min(line.start.x,line.end.x)
        right = max(line.start.x,line.end.x)
        top = min(line.start.y,line.end.y)
        bottom = max(line.start.y,line.end.y)

        if right-left == 0:
            for y in range(top,bottom):
                self.append(Point(left,y))
        elif line.end.y - line.start.y == 0:
            for x in range(left,right):
                self.append(Point(x,top))
            

def draw_rectangles(rcs):
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
rcs = [Rectangle(1,1,10,20),Rectangle(3,3,6,6)]
draw_rectangles(rcs)
draw_rectangles(rcs)

#-- The problem is if we call draw_rectangle twice, it will create the temporary objects again

    

