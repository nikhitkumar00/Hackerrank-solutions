n = input()
count = 0
for i in n:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print(count)
