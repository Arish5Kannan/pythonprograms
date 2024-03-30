string = input("Enter the string: ")
c = list(string)
d = []
for i in c:
    if ord(i)>=65 and ord(i)<=90:
       v = ord(i)+32
       d.append(chr(v))
    else:
        v = ord(i)-32
        d.append(chr(v))
def p():
  for i in d:
    print(i,end="")
print("Toogled string: ")
p()