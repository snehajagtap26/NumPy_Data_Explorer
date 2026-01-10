import numpy as np

print("\n--- RESHAPING & BROADCASTING ---")

arr = np.arange(1, 13)
print("Original Array:", arr)

reshaped = arr.reshape(3, 4)
print("Reshaped Array:\n", reshaped)

add_array = np.array([10, 20, 30, 40])
result = reshaped + add_array

print("Broadcasting Result:\n", result)
