class Student:
    def __init__(self):
        print("Constructor called")
    def Area(self,length,breath):
        print(length//breath)
try :
   s = Student()
   s.Area(4,2)
except ZeroDivisionError:
    print("Zero division occurs")
else:
    print('No Exception')
finally:
    print("Always Executed")
