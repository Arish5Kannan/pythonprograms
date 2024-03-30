s = input("Enter the string:")
l = u = n = S = 0
for i in s:
    if ord(i) >= 97 and ord(i) <= 122:
        l += 1
    elif ord(i) >= 65 and ord(i) <= 90:
        u += 1
    elif ord(i) >= 48 and ord(i) <= 57:
        n += 1
    elif ord(i)==32:
        S += 1
d = len(s.split("\n"))
e = len(s.split())
f = len(s)-(l+u+n+S)
print("Length of string:", len(s))
print("Count of \nLowercase:%d\nUppercase:%d\nNumbers:%d\nSpace:%d\nNewline:%d\nWords:%d\nSymbols:%d\n"%(l,u,n,S,d,e,f))
