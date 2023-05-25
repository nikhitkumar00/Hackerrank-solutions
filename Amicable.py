m = 220
n = 284

sum1 = 0
for i in range(1, m//2+1):
    if (m % i == 0):
        sum1 = sum1 + i
print(sum1)

sum2 = 0
for j in range(1, n//2+1):
    if (n % j == 0):
        sum2 = sum2 + j
print(sum2)

if (sum1 == n and sum2 == m):
    print('Amicable')
else:
    print('Not Amicable')
