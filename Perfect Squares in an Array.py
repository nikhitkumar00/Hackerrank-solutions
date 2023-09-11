l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 625]
count = 0
for i in l:
    if i > 0:
        temp = i
        num = 1
        while temp > 0:
            temp -= num
            num += 2
        if temp == 0:
            count += 1
print(count)
