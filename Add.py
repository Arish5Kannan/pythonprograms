""""# Using math.sqrt
import math
import numpy

sqrt_lambda = lambda x: math.sqrt(x)

# Using power operator
sqrt_lambda_alt = lambda x: x ** 0.5

# Example usage
number = 25
result = sqrt_lambda(number)
result_alt = sqrt_lambda_alt(number)

print(f"The square root of {number} is {result}")
print(f"Alternative calculation: {result_alt}")"""
def insertion(arr):
    for i in range(1,len(arr)):
        position = i
        currentvalue = arr[i]
        while(position>0 and arr[position-1]>currentvalue):
            arr[position] = arr[position-1]
            position -= 1
        arr[position] = currentvalue
arr = [3,7,1,2,0,7,5,0,2]
insertion(arr)
print(arr)

