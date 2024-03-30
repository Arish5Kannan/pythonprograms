def squareroot(num,epsilon=1e-10):
    guess = num/2.0
    while abs(guess*guess-num)>epsilon:
        guess = (guess+num/guess)/2.0
    return guess
Num = int(input("Enter the number to find square root: "))
res = (squareroot(Num))
print("Square root of %d is %.2f"%(Num,res))