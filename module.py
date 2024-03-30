from mergesort import *
List = list(map(int,input("Enter the list elemnts: ").split()))
n = len(List)
mergesort(List,0,n-1)
print([i for i in List])
import Numberpattern
n = int(input('Enter the rows for your pattern: '))
Numberpattern.pattern(n)

