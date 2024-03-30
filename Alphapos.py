str = input("Enter Single character: ").strip()[0]
print("Position of %s is %d in ascending order alphabet position"%(str,ord(str)&31))
x=ord(str)&31
print(f"Position of {str}:{x}")
print(f"Alphabet {str} position : {x}")