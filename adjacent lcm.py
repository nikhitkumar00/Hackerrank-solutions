def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i


l = [2, 4, 8, 16, 32]
s = set()

for i in range(len(l) - 1):
    s.add(lcm(l[i], l[i + 1]))
print(min(s), max(s))
