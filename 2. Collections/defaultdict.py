from collections import defaultdict


#Using a Function as Default Response
def defaultVal():
    return "Not Present"
d = defaultdict(defaultVal)
d["a"] = 100
d["b"] = 200

print(d["a"])
print(d["e"])

#Using a Function as Default Response

d = defaultdict(lambda : "Default Ret")
d["a"] = 100
d["b"] = 200

print(d["a"])
print(d["e"])

#We can use List to initialize defaultDict

d = defaultdict(list)
for i in range(5):
    d[i].append(i)

print(d)
print(d[0])
print(d[7])

#Default the value to 0
d1 = defaultdict(int)