l = [10,20,20,20,10,10,30,30,30]
dict1 = {}

for ele in l:
    if ele in dict1:
        dict1[ele] += 1
    else:
        dict1[ele] = 1

for key in dict1:
    print(key,dict1[key])