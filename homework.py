# Finding largest number among three numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a!=b and a!=c:
    if a>b and a>c :

        print("Number A is larger than B and C")
    elif b>c :

        print("B is larger than A and C")

    else:
        print("C is larger than A and B")
else:
    print("We cant find the largest number among three number. because, they are equal")
