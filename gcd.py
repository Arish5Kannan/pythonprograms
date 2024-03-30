n1,n2 =map(int,input("Enter values for two integer: ").split())
result = 0
if n1>n2:
    result = n1
else:
    result = n2
while(result>0):
    if(n1%result==0 and n2%result==0):
        break
    result -= 1
print(f"GCD : {result}")