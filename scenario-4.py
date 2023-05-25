"""

Given a string S consisting of ‘*’ and ‘#’. The length of the string is variable. The task is to find the minimum number of ‘*’ or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ and ‘#’ in the input string.
(*>#): positive integer(extra stars) if number of '*' greater than number of '#'.
(#>*): negative integer(extra hash) if number of '#' greater than number of '*'.
(#=*): 0 if number of '*' and '#' are equal.

Example :
Input : ###*** → Value of S
Output : 0 → number of * and # are equal

Input Format

Get the input string.

Constraints

2 <= |S| <= 20

Output Format

Print the output based on the input.
If the input is not valid or for constraint violation print "Wrong Input".

Sample Input 0

###***

Sample Output 0

0

Sample Input 1

#*#*#*#*##

Sample Output 1

-2

"""

s = input()
counts = 0
counth = 0

if len(s) > 20 or len(s) < 2:
    print("Wrong Input")
    exit()

for i in s:
    if i == '#':
        counth += 1
    elif i == '*':
        counts += 1
    else:
        print("Wrong Input")
        exit()

print(counth-counts)