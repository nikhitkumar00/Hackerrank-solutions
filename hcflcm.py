def ggcd(l):
    large = max(l)
    for i in range(large, 0, -1):
        flag = 0
        for j in range(len(l)):
            if l[j] % i != 0:
                flag = 1
                break
        if flag == 0:
            return i


n = int(input())
m = input().split()
l = []
for i in m:
    l.append(int(i))
hcf = ggcd(l)
product = 1
for i in l:
    product = (product * i)//ggcd([product, i])
lcm = product
print(f"HCF={hcf} LCM={lcm}")
