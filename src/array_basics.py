import numpy as np

print("\n--- ARRAY CREATION & SLICING ---")

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(10, 60, 10)

print("Array 1:", arr1)
print("Array 2:", arr2)

print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Slice (1:4):", arr1[1:4])

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print("2D Array:\n", arr2d)
print("Element at (1,2):", arr2d[1, 2])
