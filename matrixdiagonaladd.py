def DIAGONAL_SUM(n, A):
    left = right = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                left = left + A[i][j]
            if i + j == n-1:
                right = right + A[i][j]
    print(left, right)


n = 3
A = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
DIAGONAL_SUM(n, A)
