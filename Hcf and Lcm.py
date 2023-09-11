m = int(input())
n = int(input())

for i in range(1, min(m, n) + 1):
    if m % i == 0 and n % i == 0:
        hcf = i

lcm = (m * n) // hcf
print(f"HCF = {hcf}\nLCM = {lcm}")
