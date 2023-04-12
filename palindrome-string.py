n = input().upper()
f = 0
r = len(n)-1
while f < r:
    if n[f] != n[r]:
        print("NOT PALINDROME")
        exit()
    f += 1
    r -= 1
print("PALINDROME")