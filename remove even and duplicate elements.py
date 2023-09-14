l = [1, 1, 2, 2, 3, 3, 4, 5, 4, 5, 6, 7, 89, 44, 10]

s = set(l)
out = 0
for i in s:
    if i % 2 != 0:
        out += 1

print(out)
