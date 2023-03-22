"""
            print this pattern while n = 5
            1 1 1 1 1 
            3 3 3 3 
            5 5 5 
            7 7 
            9 
"""

n = int(input())
count = 1
for i in range(1,n+1):
    for j in range(0,n+1-i):
        print(count,end=' ')
    count = count + 2
    print()