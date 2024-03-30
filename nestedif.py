a=int(input("Enter one number :"))
b=int(input("Enter one number :"))
if( a!=b):
    if(a>b):
        c=a + b
        print("C:",c)
        c=a-b
        print("C:",c)

    elif(a<b):
        c=a/b
        print("C:",c)
        c=a%b
        print("C:",c)
        c = a // b
        print("C:", c)
    else:
        c=a*b
        print("C:",c)