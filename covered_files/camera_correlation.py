import os
import sys
import numpy as np
import matplotlib.pyplot as plt

BIN_FILE = sys.argv[1]
os.makedirs(OUT_DIR, exist_ok=True)
with open(BIN_FILE, "rb") as f:
    data = np.frombuffer(f.read(), dtype=np.uint8)
M = np.zeros((256, 256), dtype=np.uint64)

for i in range(len(data) - 1):
    M[data[i], data[i + 1]] += 1
M = M / M.sum()
#Heatmap ting innit
plt.figure(figsize=(11, 9))
plt.imshow(M, cmap="hot", interpolation="nearest", aspect="auto")
plt.colorbar(label="Transition probability")

plt.xlabel("Next byte value")
plt.ylabel("Current byte value")
plt.title("Byte-to-byte correlation heatmap (camera entropy)")
resulting_png = f"figures/heatmap_ting.png"
plt.savefig(resulting_png)
plt.close()

