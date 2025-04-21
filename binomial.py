from math import comb

# Parameter distribusi binomial
n = 10  # jumlah percobaan
p = 0.1  # probabilitas sukses per percobaan

# Inisialisasi total dan list hasil
total = 0
print("Distribusi Probabilitas Binomial (n=10, p=0.1):\n")
print(f"{'x':>2} | {'P(X = x)':>15}")
print("-" * 20)

for x in range(n + 1):
    prob = comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
    total += prob
    print(f"{x:>2} | {prob:>15.10f} ")

print("\nTotal Probabilitas:", total)

