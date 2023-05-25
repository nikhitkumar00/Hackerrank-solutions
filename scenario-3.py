"""

A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

Example :
N=8 and arr = [4, 5, 0, 1, 9, 0, 5, 0]
There are 3 empty packets in the given set. These 3 empty packets represented as 0 should be pushed towards the end of the array.

Input Format:
Example 1:
8 → Value of N
[4, 5, 0, 1, 9, 0, 5, 0] → Element of arr[0] to arr[N-1], and each input element is separated by newline.

Output Format :

Example 1:

4 5 1 9 5 0 0 0

Input Format

NA

Constraints

NA

Output Format

NA

Sample Input 0

8
4
5
0
1
9
0
5
0

Sample Output 0

4 5 1 9 5 0 0 0

Sample Input 1

5
10
0
20
0
30

Sample Output 1

10 20 30 0 0

"""

l = []
flag = 0

n = int(input())

for i in range(n):
    temp = int(input())
    l.append(temp)

for i in l:
    if i == 0:
        flag = flag + 1
        continue
    print(i,end=' ')
for i in range(flag):
    print('0',end=' ')