rows = int(input("Enter row size:"))
k = (2*rows)-2
for i in range(0,rows+1):
    for j in range(1,k):
        print(end=" ")
    k = k-1
    for h in range(1,i+1):
        print("*",end=" ")
    print("")
k = rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k += 1
    for j in range(1,i):
        print("*",end=" ")
    print("")
