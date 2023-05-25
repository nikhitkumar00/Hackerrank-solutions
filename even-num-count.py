"""
    Write code for finding the sum of all even integer numbers in the given string.

    Input Format
        Input the string of length M in line 1.

    Constraints
        NA

    Output Format
        Output the sum of all even integer numbers in the given string.

    Sample Input 0
        Whe9re are yo1u?

    Sample Output 0
        0

    Sample Input 1
        Daya123Ben456
        
    Sample Output 1
        12
"""

count = 0
n = input()
for i in n:
    if i.isnumeric() and int(i) % 2 == 0:
        count += int(i)
print(count)
