# Matrix multiplication and find eigen value and eigen vector using TensorFlow
#Code:
print("Name:- Manish choudhary ")
print("Roll No :- 10")
import numpy as np
import torch
import tensorflow as tf
print("matrix multiplication using tensorflow")
x = tf.constant([1,2,3,4,5,6],shape=[2,3])
y = tf.constant([7,9,8,10,11,12],shape=[3,2])
print("x=",x)
print("y=",y)
z = tf.matmul(x,y)
print("multiplication of x & y= ", z)
ematrix = tf.random.uniform([2,2], minval =3,maxval=10,dtype= tf.float32, name ="matrixA")
print("Matrix A= {} \n\n".format(ematrix))
evalue, evector = tf.linalg.eigh(ematrix)
print("Eign Vectors:{}\n\n Eign value:{}\n" .format(evector,evalue))
