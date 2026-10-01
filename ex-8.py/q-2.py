#WAP for data types and structures in NumPy
import numpy as np

# Data types
a = np.array([1, 2, 3], dtype=int)
b = np.array([1.5, 2.5, 3.5], dtype=float)
c = np.array([True, False, True], dtype=bool)

print("Integer:", a, a.dtype)
print("Float:", b, b.dtype)
print("Boolean:", c, c.dtype)

# Data structures
print("1D Array:", np.array([1, 2, 3]))
print("2D Array:", np.array([[1, 2], [3, 4]]))
print("3D Array:", np.array([[[1, 2], [3, 4]]]))
