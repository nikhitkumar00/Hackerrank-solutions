l = [1, 1, 2, 2, 3, 3, 4, 5, 4, 5, 6, 7, 89, 44, 10]

dic = {}
try:
    i = 0
    while 1:
        if l[i] % 2 == 0:
            l.pop(i)
        else:
            if l[i] in dic:
                l.pop(i)
            else:
                dic[l[i]] = 1
                i += 1
except:
    print(l)
