"""n = int(input("Enter the number:"))
rev=0
while n!=0:
 rem=n%10#121%10=1,12%10=2,1%10=1
 rev=(rev*10)+rem#rev=(0*10)+1=1,rev=(1*10)+2=12,rev=(12*10)+1
 n/=10#121/10=12,12/10=1,1/10=0
#loop ending
print("Reversed number:",rev)"""
"""
#rev=0
num=int(input("Enter the number:"))
while num!=0:
    rem=rev*10
    rev=rem+(num%10)
    num=num/10
print("Reversed number:",rev)
"""

"""a=int(input("Enter a value:"))
b= int(input("Enter b value:"))
print("Before swapping , A value:",a," and ","B value :",b)
a=a+b
b=a-b
a=a-b
print("After swapping , A value:",a," and ","B value :",b)"""
a=int(input("Enter a value:"))
b= int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a>b and a>c:
    print("A ",a," is greater than b and c")
elif b>c:
    print("B ",b," is greater than a and c")
else:
    print("c",c," is greater than a and b")


