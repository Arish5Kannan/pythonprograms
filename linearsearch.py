L = list(map(int,input('Enter list elements: ').split(" ")))
num = int(input('Enter number to search in the list: '))
found = False
for i in range(0,len(L)):
    if L[i] == num:
        found = True
        index = i
        break
if  found == True:
    print(f"Value {num} is found at L[{index}] in the list")
else:
    print(f"Value {num} is not found in the list")