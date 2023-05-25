# print numbers upto n which is not divisible by 3 or 5

n = int(input())
for i in range(1, n+1):
    if (i % 3 != 0 and i % 5 != 0):
        continue
    print(i, end=' ')
