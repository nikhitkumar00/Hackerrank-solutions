"""
Mr. Geek was given a list of marks scored by the students who attended a test. Teacher wants Geek to arrange all the marks in the same order but he has to move all the zeros to the end of the list and find the average marks excluding the zero mark scored students. Average marks should be appended at the end of output list. He can ignore the decimal part of the average marks while appending. As a programmer you are asked by the Geek to help him to write a code for doing the same.
Expected time complexity is O(n) and extra space is O(1).
Sample Input and Output:
Input: 45 30 0 25 10 0 90 95 0 50
Output: 45 30 25 10 90 95 50 0 0 0 49

Input Format

Size of the array(N) and line separated array input elements are already taken.
An array is made out of those elements and given the name "marks" and is given as input parameter to the function.
You are not supposed to take any input.

Constraints

NA

Output Format

Return the list with all the test marks in the same order as in the input list by pushing all the zero marks towards the end of the list.
The average marks excluding the zero mark scored students should have been appended to the returning list.

Sample Input 0

5
1 
0 
2 
0 
3 
Sample Output 0

1 2 3 0 0 2
Sample Input 1

10
100 
90 
80 
0 
0 
70 
60 
0 
50 
40 
Sample Output 1

100 90 80 70 60 50 40 0 0 0 70
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'GEEK_MARKS' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY marks as parameter.
#


def GEEK_MARKS(marks):
    nz = 0
    sum = 0
    for i in range(len(marks)):
        if (marks[i] != 0):
            marks[nz] = marks[i]
            sum = sum + marks[i]
            nz = nz + 1
    avg = sum//nz
    while (nz < len(marks)):
        marks[nz] = 0
        nz = nz + 1
    marks.append(avg)
    return marks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    marks = []

    for _ in range(n):
        marks_item = int(input().strip())
        marks.append(marks_item)

    mod_marks = GEEK_MARKS(marks)

    fptr.write(' '.join(map(str, mod_marks)))
    fptr.write('\n')

    fptr.close()
