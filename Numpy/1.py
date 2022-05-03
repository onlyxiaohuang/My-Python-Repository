#Use numpy to get a random array
import numpy as np

data = np.random.randn(2,3)#random float 
print(data)

data2 = np.random.randint(1,10)#random integers
print(data2)
Array = np.array(data2)
Array = Array.astype(np.int32)
print(Array)

#use numpy to get a array
List1 = [ [2,3] , [9,8] , [0,12] ]# the length must be the same
Array1 = np.array(List1)
print(Array1)

Array2 = np.zeros(10)
print(Array2)

Array3 = np.ones(10)
print(Array3)

Array4 = np.arange(15)
print(Array4)
print(Array4.dtype)