"""
A parking lot in a mall has R x C number of parking spaces. Each parking space will either be empty(0) or full(1). The status (0/1) of a parking space is represented as the element of the matrix. The task is to find index of the first parking row(R) in the parking lot that has the most of the parking spaces full(1).

Note :
R x C - Size of the matrix.
Elements of the matrix M should be only 0 or 1.

Example 1:
Input :
3 → Value of R(row)
3 → value of C(column)
[0 1 0 1 1 0 1 1 1] → Elements of the array M[R][C] where each element is separated by new line.

Output :
3 → Row 3 has maximum number of 1's

Input Format

NA

Constraints

NA

Output Format

If all the parking slots are free print "0" else print the index of the first parking row(R) in the parking lot that has the most of the parking spaces full(1).

Sample Input 0

3
3
0
1
0
1
1
0
1
1
1

Sample Output 0

3

Sample Input 1

4
3
0
1
0
1
1
0
1
0
1
1
1
1

Sample Output 1

4

"""

m = int(input())
n = int(input())
s = []

l = [[int(input()) for j in range(n)] for i in range(m)]
for i in range(m):
    flag = 0
    for j in range(n):
        if l[i][j] == 1:
            flag = flag + 1
    s.append(flag)

large = -1
for i in range(len(s)):
    if s[i] > large:
        large = s[i]
        index = i
print(index+1)
