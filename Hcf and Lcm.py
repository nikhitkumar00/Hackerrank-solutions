m = int(input())
n = int(input())

min = min(m, n)

for i in range(1, min+1):
    if (m % i == 0 and n % i == 0):
        hcf = i

lcm = int((m*n)/hcf)


print('HCF = {}\nLCM = {}'.format(hcf, lcm))
