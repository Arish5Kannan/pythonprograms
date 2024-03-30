class Father():
    def father(self):
        print("Money in fathers hand")
class Son(Father):
    def son(self):
        print("Son has empty hand")
class Sinherit():
    print("Single Inheritance")
    A = Son()
    A.son()
    A.father()
