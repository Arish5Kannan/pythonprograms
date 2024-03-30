f = open("Add.py",'w')
f.close()
n = int(input('Enter the range:'))
Limit = int(input())
for num in range(n,Limit+1):
    temp = num
    S = 0
    while num > 0:
        rem = num % 10
        fact = 1
        for i in range(1, rem + 1):
            fact = fact * i
        S = S + fact
        num //= 10
    if S== temp:
        print(f"{S} is strong number")


