import csv
import os
import matplotlib.pyplot as plt

CSV_FILE = "rsa_camera_results.csv"  
OUT_DIR = "figures"

os.makedirs(OUT_DIR, exist_ok=True)

leading_bytes = []

with open(CSV_FILE, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        N = int(row["modulus_hex"], 16)
        bitlen = N.bit_length()
        top_byte = (N >> (bitlen - 8)) & 0xFF
        leading_bytes.append(top_byte)

plt.figure(figsize=(9, 7))
plt.hist(
    leading_bytes,
    bins=256,
    range=(0, 256)
)

plt.xlabel("Top 8 bits of modulus")
plt.ylabel("Count")
plt.title("Leading-bit distribution of RSA moduli")
plt.xlim(0, 255)
plt.grid(axis="y", linestyle=":", alpha=0.3)
plt.tight_layout()

resulting_png = f"{OUT_DIR}/rsa_modulus_leading_8bits.png"

plt.savefig(resulting_png)
plt.close()


