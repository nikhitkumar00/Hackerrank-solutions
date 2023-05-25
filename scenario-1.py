"""
Simmi loves to solve problems. Hence on her birthday, her friend asked to write code for an interesting problem. She gave some positive integer numbers to Simmi in sorted(ascending) order and asked her to rearrange the numbers alternately, i.e first number should be maximum value, second minimum value, third second max, fourth second min and so on. You are assigned to help Simmi to solve this problem.

Input Format

Get the count of sorted numbers as input.
Get the sorted numbers as input.

Constraints

NA

Output Format

Output the rearranged array as mentioned in the problem statement.

Sample Input 0

7
1 2 3 4 5 6 7

Sample Output 0

7 1 6 2 5 3 4

Sample Input 1

6
1 2 3 4 5 6

Sample Output 1

6 1 5 2 4 3

"""

n = int(input())
l = input().split()

min = 0
max = n-1
i = 0
while(min<=max):
    if i%2==0:
        print(l[max],end=' ')
        max = max - 1
    else:
        print(l[min],end=' ') 
        min = min + 1   
    i = i + 1