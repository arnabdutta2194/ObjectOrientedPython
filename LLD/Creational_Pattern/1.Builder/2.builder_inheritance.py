#---Problem with single or multiple builders were, everytime we have a new sub builder, we need to add it to the main builder
#--- This was directly violating Open Closed principle

#--- Alternative approach is to use builder inheritance


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None
    
    def __str__(self) -> str:
        return f'{self.name} born on {self.date_of_birth} and works as {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()
    
class PersonBuilder:
    def __init__(self):
        self.person = Person()
    
    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self,name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works(self,job):
        self.person.position = job
        return self

class PersonDOBBuilder(PersonJobBuilder):
    def dob(self,dob):
        self.person.date_of_birth = dob
        return self


#--- When we expand our model we can simply keep on inheriting without breaking Open Closed Principle

pb = PersonDOBBuilder()
me = pb.called('Arnab').works('SDE II').dob('1997-07-24').build()
print(me)
