#--- Polymorphism comes with a concept of overriding which changes the behaviour of your BaseClassMethod within the Derived Clas
#--- super() allows you to access any Attributes or Methods from your Base Class


class Employee:
    def setNumberofWorkingHours(self):
        self.numberofWorkngHours = 45
    def displayNumberOfWorkingHours(self):
        print(self.numberofWorkngHours)


class Trainee(Employee):
    def setNumberofWorkingHours(self):
        self.numberofWorkngHours = 40 #--- Method overriding
    def resetNumberofWorkingHours(self):
        super().setNumberofWorkingHours()

emp = Employee()
emp.setNumberofWorkingHours()
print("Number of Working Hours for Employee",end=' ')
emp.displayNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberofWorkingHours()
print("Number of Working Hours for Trainee",end=' ')
trainee.displayNumberOfWorkingHours()

trainee.resetNumberofWorkingHours()
print("Number of Working Hours for Trainee after reset",end=' ')
trainee.displayNumberOfWorkingHours()


print("***********************************")

#--- Overloading

class Square():
    def __init__(self,side) -> None :
        self.side= side
    def __add__(squareOne,squareTwo):
        return((4*squareOne.side) + (4*squareTwo.side))

squareOne = Square(5)
squareTwo = Square(10)

print("Sum of sides of a both the squares =", squareOne + squareTwo)
#--- Above execution will give unsupported operand types