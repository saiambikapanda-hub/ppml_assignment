#WAP for NumPy array properties and functions
import numpy as np

# Create array
a = np.array([[10, 20, 30],
              [40, 50, 60]])

# Array properties
print("Array:", a)
print("Dimension:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)
print("Data Type:", a.dtype)

# Array functions
print("Sum:", np.sum(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Mean:", np.mean(a))
