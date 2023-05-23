"""
Write code for printing every distinct number in an input array with the frequency of their occurrence.
Sample Array:10 20 30 40 50 10 30 50
Output
10 2
20 1
30 2
40 1
50 2

Input Format

Size of the array(N) and space separated array input is already taken and an array called 'L' is made out of the inputs.
This array 'L' is given as input parameter to the function.
You are not supposed to take any input.

Constraints

NA

Output Format

Print the distinct numbers in the order of their occurrence in the array with its frequency of occurrence in the function itself.

Sample Input 0

5
10 20 10 20 30
Sample Output 0

10 2
20 2
30 1
Sample Input 1

5
300 200 100 200 100
Sample Output 1

300 1
200 2
100 
"""

import math
import os
import random
import re
import sys

def FREQ(L):
    dict1 = {}

    for ele in L:
        if ele in dict1:
            dict1[ele] = dict1[ele] + 1
        else:
            dict1[ele] = 1

    for key in dict1:
        print(key,dict1[key])

if __name__ == '__main__':
    n = int(input().strip())

    L = list(map(int, input().rstrip().split()))

    FREQ(L)
