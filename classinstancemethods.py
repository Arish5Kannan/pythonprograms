class A:
    name = 'Arish'
    age = 18
    def printall(self, gender):
        print("Name : ",A.name)
        print("Age : ",A.age)
        print("Gender : ",gender)
s = A()
A.printall(s,"Female")
s.printall("Male")
