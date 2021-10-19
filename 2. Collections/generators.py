def sq_numbers(n):
    for i in range(1,n+1):
        yield i*i

a = sq_numbers(3)

print(next(a))
print(next(a))
print(next(a))


def func():
    i=1
    while i>0:
        yield i
        i-=1
for i in func():
    print(i)
print(func().__sizeof__())