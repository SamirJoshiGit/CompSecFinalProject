import sys
import os
import numpy as np
import matplotlib.pyplot as plt

binary = sys.argv[1]
label = sys.argv[2]
with open(binary, "rb") as f:
    data = np.frombuffer(f.read(), dtype=np.uint8)

counts = np.bincount(data, minlength=256)
total = len(data)
expected = total / 256.0

plt.figure(figsize=(11, 5))
plt.bar(range(256), counts, width=1.0, edgecolor="black")
plt.axhline(expected, color="red", linestyle="--", label="Expected uniform count")

plt.xlabel("Byte value (0–255)")
plt.ylabel("Count")
plt.title(f"Byte frequency distribution ({label})")
plt.legend()
plt.tight_layout()

resulting_png = f"figures/byte_distribution_{label}.png"
plt.savefig(resulting_png)
plt.close()

