i,n = map(int,input("Enter the range:").split("-"))
for i in range(i,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count==2:
        print(f"{i} is prime number")

