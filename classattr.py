class Student():
    name = "Arish"
    age = 7
print(Student.name,Student.age)
Student.name = "Kannan"
Student.age = 18
print(Student.name,Student.age)
setattr(Student,'name',"Servesh")
print(Student.name,Student.age)
Student.Class = "7th"
print(Student.name,Student.age,Student.Class)
print(Student.__dict__)
delattr(Student,"name")
print(Student.age,Student.Class)
print(Student.__dict__)
del Student.Class
print(Student.__dict__)