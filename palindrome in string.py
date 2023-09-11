s = "ABCBAAAA"
points = 0
for i in range(len(s)):
    if i + 3 < len(s) and s[i : i + 4] == s[i : i + 4][::-1]:
        points += 5
    if i + 4 < len(s) and s[i : i + 5] == s[i : i + 5][::-1]:
        points += 10
print(points)
