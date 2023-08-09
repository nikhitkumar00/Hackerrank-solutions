"""
    https://www.hackerrank.com/contests/manifold-20/challenges/array-1-2/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def GEEK_MARKS(marks):
    
    sum = 0
    count = len(marks)
    i = 0;num = 0
    while(num != len(marks)):
        if marks[i] == 0:
            marks.remove(0)
            marks.append(0)
            count -= 1
        else:
            sum += marks[i]
            i += 1
        num += 1
    avg = sum//count
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