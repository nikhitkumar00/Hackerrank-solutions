# n = int(input())
# l = [input().split()]


def gcd(l):
    large = max(l)
    for i in range(large, 0, -1):
        flag = 0
        for j in range(len(l)):
            if l[j] % i != 0:
                flag = 1
                break
        if flag == 0:
            return i

l = [184,230,276]
hcf = gcd(l)
product = 1
for i in l:
    product = (product * i)//gcd([product,i])
lcm = product
print(hcf,lcm)
