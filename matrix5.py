n = int(input())
a = [[int(input()) for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        print(a[j][i], end=' ')
    print()
