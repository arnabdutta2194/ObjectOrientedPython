from collections import ChainMap

d1 = {'a':1,'b':2}
d2 = {'c':3,'d':5}
d3 = {'e':4,'g':8}

c = ChainMap(d1,d2,d3)
print(c)

print(c.maps) #Provides list of all the dictionaries
print(list(c.keys()))
print(c.values())