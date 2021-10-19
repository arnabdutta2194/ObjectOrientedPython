class A:
    def func(self):
        return "A.func()"
class B(A):
    def func(self):
        return "B.func()"
class C(A):
    def func(self):
        return "C.func()"
# class D(B,C):
#     pass
# d = D()

class D(C,B):
    pass
d = D()

print(d.func())