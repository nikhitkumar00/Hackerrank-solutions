n = int(input())
dict = {}
for i in range(n):
    l = input().split()
    dict[l[0]] = int(l[1])
try:
    while(1):
        n = input()
        if n == "":
            break
        elif n in dict:
            print(f"{n}={dict[n]}")
        else:
            print("Not found")
except:
    exit()