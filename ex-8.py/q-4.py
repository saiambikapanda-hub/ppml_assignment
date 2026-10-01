#WAp for statistical operations and broadcasting on arrays
import numpy as np

# Create array
a = np.array([[10, 20, 30],
              [40, 50, 60]])

# Statistical operations
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Standard Deviation:", np.std(a))

# Broadcasting
b = np.array([1, 2, 3])
print("After Broadcasting:")
print(a + b)
