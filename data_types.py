import numpy as np 

#integers

i=10 #integer
print("The data type of i is ",type(i)) #int


a_i = np.zeros(i,dtype=int) #declare an array of zeroes
print("The data type of a_i is ",type(a_i)) #np.ndarray
print("The data type of a_i[0] is ",type(a_i[0])) #int64


 #floats

x = 119.0
print("The data type of x is ",type(x)) #data type of x

y = 1.19e2 #float 119 in scientific notation
print("The data type of y is ",type(y)) #data type of y

z = np.zeros(i,dtype=float) #declare array of floats
print(type(z))
print(type(z[0]))