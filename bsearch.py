"""
def bsearch(arr,x):
 low = 0
 high = len(arr)
 while(low<=high):
     mid = (low+high)//2
     if arr[mid] == x:
         return mid
     elif x<arr[mid]:
         high = mid-1
     else:
         low = mid+1
 return -1
arr = list(map(int,input("Enter elements:").split()))
num = int(input("Enter the number to search:"))
res = bsearch(arr,num)
if res != -1:
    print(f"Element {num} is present at arr[{res}]")
else:
    print(f"Element {num} is not present in arr")
    """
def fun(n):
    if  n <= 1:
        return n
    else:
        return (fun(n-1)+fun(n-2))
print("Fibonacci series:")
for i in range(5):
    print(fun(i),end=" ")

