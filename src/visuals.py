import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# FIXED DATASET (VERY IMPORTANT)
# -----------------------------
data = np.array([88, 60, 88, 36, 74, 91, 81, 63, 73, 27])
index = np.arange(len(data))


# =============================
# 1. HISTOGRAM - Data Distribution
# =============================
plt.figure()
plt.hist(data, bins=5)
plt.title("Histogram - Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


# =============================
# 2. BAR GRAPH - Random Dataset
# =============================
plt.figure()
plt.bar(index, data)
plt.title("Bar Graph - Random Dataset")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()


# =============================
# 3. LINE GRAPH - Random Dataset
# =============================
plt.figure()
plt.plot(index, data)
plt.title("Line Graph - Random Dataset")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()
