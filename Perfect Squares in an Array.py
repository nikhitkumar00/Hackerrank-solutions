def checkPerfectSquare(N):
    if N < 0:
        return 0

    i = 1
    while N > 0:
        N -= i
        i += 2

    return 1 if N == 0 else 0


N = int(input())
print(checkPerfectSquare(N))
