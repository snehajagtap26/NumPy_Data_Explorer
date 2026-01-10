import numpy as np

print("\n--- MATHEMATICAL & STATISTICAL OPERATIONS ---")

data = np.array([10, 20, 30, 40, 50])

print("Data:", data)
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Standard Deviation:", np.std(data))

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Column-wise Sum:", np.sum(matrix, axis=0))
print("Row-wise Sum:", np.sum(matrix, axis=1))
