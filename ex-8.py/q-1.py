#WAP for ndarray object,Indexing and Slicing
import numpy as np

a = np.array([[10,20,30],[40,50,60]])

# Properties
print(a.ndim, a.shape, a.size, a.dtype)

# Indexing
print(a[0,1])

# Slicing
print(a[:,1:])

# Arithmetic operations
print(a + 10)
print(a * 2)

# Statistical functions
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))

# Broadcasting
b = np.array([1,2,3])
print(a + b)

# Logical operations
print(a > 30)
print(a[a > 30])
0