from collections import Counter

z = ['red','blue','green','red','green','black','red']
print(Counter(z))

#Alternative of Above implementation
coun = Counter()
coun.update(z)
print(coun)


lst1 = ['red','blue','green','red','green','black','red']
lst2 = ['red','blue','blue','red','green','black','yellow']

c1 = Counter(lst1)
c2 = Counter(lst2)
print(c1)
print(c2)
print(c2.subtract(c1))


# To find 2 most common elements
print(c1.most_common(2))
print(c1["red"])

#If key does not exist Value will default to 0
print(c1["purple"])