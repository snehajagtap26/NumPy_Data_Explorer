import numpy as np
import time

print("\n--- PERFORMANCE COMPARISON ---")

size = 1_000_000

py_list = list(range(size))
start = time.time()
py_list = [x * 2 for x in py_list]
print("Python List Time:", time.time() - start)

np_array = np.arange(size)
start = time.time()
np_array = np_array * 2
print("NumPy Array Time:", time.time() - start)
