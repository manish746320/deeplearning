#➢ Demonstrate Vectors and Perform the following operations
print ("Manish choudhary, Roll no 10")
import numpy as np
#declaring vectors
x = [1,2,3]
y = [4,5,6]
print("x=",x)
print("y=",y)
print(type(x))
#for addition
print(x+y)
#vector addition using numpy
z = np.add(x,y)
print("Addition=",z)
print(type(z))
#vector cross product
mul = np.cross(x,y)
print("mul=", mul)