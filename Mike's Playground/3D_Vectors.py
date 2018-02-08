#Create a way to mathematically calculate 3-D vectors

import math

#Calculate the magnitude of a vector

def magnitude():
    #Enter variable values
    x = float(input('Enter x value.\n>>> '))
    y = float(input('Enter y value.\n>>> '))
    z = float(input('Enter z value.\n>>> '))
    value = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    return value

result = magnitude()
print(result)
