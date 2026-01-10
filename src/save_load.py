import numpy as np

print("\n--- SAVE & LOAD NUMPY ARRAY ---")

data = np.array([100, 200, 300])
np.save("data/sample_data.npy", data)

loaded_data = np.load("data/sample_data.npy")
print("Saved & Loaded Data:", loaded_data)
