n1,n2 = map(int,input('Enter two numbers:').split())
Max = max(n1,n2)
while(1):
    if Max%n1 == 0 and Max%n2 == 0:
        print("LCM : %d"%Max)
        break
    Max += 1