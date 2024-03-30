print("Enter the range:")
i,n = map(int,input().split())
for i in range(i,n+1):
    temp = i
    digit3 = i%10
    i//=10
    digit2 = i%10
    i//=10
    digit1 = i%10
    i//=10
    res = (digit1*digit1*digit1)+(digit2*digit2*digit2)+(digit3*digit3*digit3)
    if(temp==res):
        print(f"{res} is Armstrong number")



