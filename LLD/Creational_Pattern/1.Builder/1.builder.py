class Person:
    def __init__(self):
        #address
        self.street_address = None
        self.postcode = None
        self.city = None
        #employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address {self.street_address}, {self.postcode}, {self.city}' + f'Employed At {self.company_name} as a {self.position} earning {self.annual_income}'

class PersonBuilder:
    def __init__(self,person=Person()): #---Initializing the person builder with blank person
        self.person = person
    
    @property
    def works(self):
        return PersonJobBuilder(self.person) #---Providing an instance which is already being constructed
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person) #---Multiple builders used to construct the object
    
    def build(self):
        return self.person
    
class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
    
    def at(self,company_name):
        self.person.company_name =company_name
        return self
    def as_a(self,position):
        self.person.position =position
        return self
    
    def earning(self,annual_income):
        self.person.annual_income =annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
    
    def at(self,street_addres):
        self.person.street_address =street_addres
        return self
    
    def with_postcode(self,postcode):
        self.person.postcode =postcode
        return self
    
    def in_city(self,city):
        self.person.city =city
        return self

pb = PersonBuilder()
person = pb.lives.at('PMGSY Road').in_city('Siliguri').with_postcode('734011').works.at('ABC Corp').as_a('SDE II').earning('12 LPA').build()
print(person)