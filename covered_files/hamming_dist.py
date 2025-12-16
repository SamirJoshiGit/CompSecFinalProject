import csv
import matplotlib.pyplot as plt

def hamming(a, b):
    return (a ^ b).bit_count()

values = []
with open("rsa_keys.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        values.append(int(row["modulus"], 16))

dists = [hamming(values[i], values[i+1]) for i in range(len(values)-1)]

plt.figure()
plt.hist(dists, bins=30, edgecolor="black")
plt.xlabel("Hamming distance between consecutive moduli (bits)")
plt.ylabel("Count")
plt.title("RSA modulus Hamming distance")
plt.tight_layout()
plt.savefig("hamming_hist.png", dpi=300)

print("Avg distance:", sum(dists)/len(dists))

