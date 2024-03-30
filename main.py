"""def is_prime(n):
    c = 0
    for j in range(1,n+1):
        if n%j == 0:
            c += 1
    if c == 2:
        return 1
    else:
        return 0
n = int(input("Enter the number: "))
check = is_prime(n)
if check == 1:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")"""
"""a = int(input())
b = int(input())
s = lambda x,y: x*y
print(s(a,b))"""
"""def concat(n):
    if n>0:
        c[n] = input("Input the string: ")
        n -= 1
        concat(n)
    else:
        c[3] = c[2] + c[1]
        print(c[3])
c = [1,2,3,4,5]
concat(2)"""
def abc(n):
    s = []
    for i in range(n):
        a = int(input())
        s.append(a)
    if s[0] == 0:
        print("True")
    elif s[1] == 0:
        print("True")
    elif s[2] == 0:
        print("True")
    else:
        print("False")
abc(3)



