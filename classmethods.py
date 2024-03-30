class A:
    name = 'Arish'
    Age = 18
    def printall():
        print("Name: ",A.name)
        print("Age: ",A.Age)
A.printall()
print(A.__dict__)
getattr(A,"printall")()
A.__dict__["printall"]()