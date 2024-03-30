class Grandpa():
    def grand(self):
        print("Grandpa sold property")
class Father(Grandpa):
    def father(self):
        print("Money in fathers hand")
class Son(Father):
    def son(self):
        print("Son has empty hand")
class MLinherit():
    print("Multilevel Inheritance")
    A = Son()
    A.son()
    A.father()
    A.grand()