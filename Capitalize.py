string = input("Enter the string: ")
c = list(string)
if ord(c[0])>=97 and ord(c[0])<=122:
    c[0] = chr(ord(c[0])-32)
i = 1
while i<len(c):
    if ord(c[i]) == 32:
       i += 1
       if ord(c[i])>=97 and ord(c[i])<=122:
         c[i] = chr(ord(c[i])-32)
    else:
        if ord(c[i])>=65 and ord(c[i])<=90:
            c[i] = chr(ord(c[i])+32)
    i += 1
for i in c:
    print(i,end="")