#Normal Array 
arr1 = [10,11,12,13,14,15]
for i in arr1:
    print(i)

print("*****")

#Using Iterators 
iterList = iter(['My','Name','is','Arnab'])
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))


## Memory Consumption By Iterators

print(iterList.__sizeof__())