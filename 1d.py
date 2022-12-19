# Demonstration of following Matrices:
#Addition of matrices
#Multiplication
#Transpose
print("Name:- Manish choudhary ")
print("Roll No :- 10")
import numpy as np
from numpy import matrix
m1=np.matrix([[1,2,3],[2,3,7],[8,9,2]])
print("matrix1=",m1)
m2=np.matrix([[5,4,3],[8,2,5],[3,7,1]])
print("matrix2=",m2)
addition = np.add(m1,m2)
print("matrix addition=",addition)
multiplication=np.matmul(m1,m2)
print("matrix multiplication=",multiplication)
transpose1=np.transpose(m1)
print("transpose of m1 =",transpose1)
transpose2=np.transpose(m2)
print("transpose of m2 =",transpose2)