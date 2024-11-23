#--- The problem with standard prototype implementation is that , we keep building objects using deepcopy which is not a good approach
#--- Instead we can give factory methods to build objects

import copy

class Address:
    def __init__(self,city,emp_id,country):
        self.city = city
        self.emp_id =emp_id
        self.country = country

    def __str__(self):
        return f'{self.city,self.emp_id,self.country}'


class Employee:
    def __init__(self,name,address):
        self.name = name
        self.address =address

    def __str__(self):
        return f'{self.name} lives in {self.address}'
    
class Employeefactory:
    main_office_employee = Employee('',Address('London','','UK'))
    aux_office_employee = Employee('',Address('Chelsea','','UK'))

    @staticmethod
    def __new_employee(proto,name,emp_id):
        result = copy.deepcopy(proto)
        result.name = name
        result.emp_id = emp_id
        return result


    @staticmethod
    def new_main_office_employee(name,emp_id):
        return Employeefactory.__new_employee(Employeefactory.main_office_employee,name,emp_id)

    @staticmethod
    def new_aux_office_employee(name,emp_id):
        return Employeefactory.__new_employee(Employeefactory.aux_office_employee,name,emp_id)
 
main_emp = Employeefactory.new_main_office_employee('AD','112233')
print(main_emp)
aux_emp = Employeefactory.new_aux_office_employee('RK','E12345')
print(aux_emp)