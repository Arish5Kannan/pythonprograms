class A:
    course = 'java'
print(A.course)
print(A.__dict__)
B = A()
print(B.__dict__)
B.course = 'c++'
B.sno = 1
print(B.__dict__)
