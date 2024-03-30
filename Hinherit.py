class Father():
    def fa(self):
        print("Father property")
class Son1(Father):
    def s1(self):
        print("Son1 accessed father property")
class Son2(Father):
    def s2(self):
        print("Son2 accessed father property")
class Son3(Father):
    def s3(self):
        print("Son3 accessed father property")
A = Son1()
B = Son2()
C = Son3()
A.s1()
A.fa()
B.s2()
B.fa()
C.s3()
C.fa()