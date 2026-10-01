#WAP for saving and loading arrays
import numpy as np

# Create array
a = np.array([10, 20, 30, 40, 50])

# Save array
np.save("data.npy", a)

# Load array
b = np.load("data.npy")

print("Original Array:", a)
print("Loaded Array:", b)
