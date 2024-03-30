row = int(input("Enter the row size:"))
h = 65
for j in range(1,row+1):
  for i in range(0,j):
    print(chr(h),end="  ")
  h += 1
  print()
row = row-1
for j in range(row,-1,-1):
  for i in range(j,0,-1):
    print(chr(h),end="  ")
  h += 1
  print()
print("______________________________________")
h = 65
for i in range(1,row+1):
    for j in range(1,row+1):
        print(chr(h),end="  ")
    h += 1
    print("")

