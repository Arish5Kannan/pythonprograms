class Student:
    age = 18
    marks = 498
    def __int__(self):
        print("Constructor called")
    def printall(self,name):
        print("Name : ",name)
        print("Age : ",Student.age)
        print("Mark : ",Student.marks)
o = Student()
o.printall("Arish")
