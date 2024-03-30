i,n = map(int,input("Enter the range:").split("-"))
for i in range(i,n+1):
    temp = i
    Sum = 0
    for j in range(1,i):
        if i%j == 0:
            Sum = Sum + j
    if Sum == temp:
        print(f"{i} is perfect number")
