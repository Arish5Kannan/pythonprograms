"""print("Print equilateral triangle Pyramid using stars")
size = int(input("Enter the size: "))
m = (2*size)-2
for i in range(0,size):
    for j in range(0,m):
        print(end=" ")
    m = m - 1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
sides = int(input("Enter the number of rows of square:"))
for i in range(0,sides):
    for j in range(0,sides):
        print("*",end="  ")
    print("")
rows = int(input("Enter the number of rows of diamond pattern:"))
k = 2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k = k - 1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")
k = rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k = k + 1
    for j in range(0,i+1):
        print("*",end=" ")
    print("")
"""
"""n = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 0
if n<=0:
    print("Enter the positive number")
elif n==1:
    print("Fibanocci series:")
    print(n)
else:
    print("Fibanocci sequence: ")
    while(count<n):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1"""
"""n1 = int(input())
n2 = int(input())
if n1%n2 == 0:
    print("Multiple")
else:
    print("Not Multiple")"""
n = 1
n1 = 3
def swap():
    global n,n1
    (n1,n) = (n,n1)
print(f"Before swap: n = {n} n1 = {n1}")
swap()
print(f"Before swap: n = {n} n1 = {n1}")




