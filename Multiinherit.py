class Add():
    a=b=0
    def sum(self,a,b):
        self.a = a
        self.b = b
        print(f"Addition of {self.a} and {self.b} is {self.a + self.b}")
class Sub():
    a=b=0
    def sub(self,a,b):
        self.a = a
        self.b = b
        print(f"Subtraction of  {self.a} and {self.b} is", (self.a - self.b))
class Multiinherit(Add,Sub):
  pass
A = Multiinherit()
A.sum(8,3)
A.sub(8,4)




