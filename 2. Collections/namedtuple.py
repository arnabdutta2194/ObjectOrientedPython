from collections import namedtuple

Student = namedtuple("Student",['name','age','DOB'])

std1 = Student("Arnab",23,"23/07/1997")
std2 = Student(name="Arnab",age=23,DOB="23/07/1997")

print(std1.DOB)
print(std1[2])
print(getattr(std1,'DOB'))
print(std2)

#Converting Normal Iterables to Named Tuple

li = ["Arnab",21,"1221"]
std3 = Student._make(li) 
print(std3)

#Converting NamedTuple to OrderedDict

print(std3._asdict())

#To check the fields of namedtuples
print(std1._fields)
#Replacing a field Value
print(std1._replace(name = "Ronnie"))
print(std1)
