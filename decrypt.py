"""
Assume that your company is working on a project for finding a new string compression algorithm. Since you are a part of that project, team leader asked you to write a program related to string expansion. In the input string every alphabet will be followed by its count(no. of continuous occurrance) and the alphabet can be lowercase or uppercase.Your program should output the expanded string based on the count of each alphabet.

Sample Input and Output:
Input: a1b10
Output: abbbbbbbbbb

Input Format

Encrypted string 's' is given as input parameter of the function.
You are not supposed to take any input.

Constraints

NA

Output Format

Return the decrypted(expanded) string based on the count of each alphabet.

Sample Input 0

a1b2C3D4
Sample Output 0

abbCCCDDDD
Sample Input 1

A5C3D1X3
Sample Output 1

AAAAACCCDXXX
"""

import math
import os
import random
import re
import sys

def DECRYPT(s):
    i = 0
    temp = 0
    chrr = ""
    strr = ""
    while(i < len(s)):
        if s[i].isdigit():
            if i != (len(s)-1):
                if s[i+1].isdigit():
                    temp = int(s[i]+s[i+1])
                    i = i + 2
                else:
                    temp = int(s[i])
                    i = i + 1       
            else:
                temp = int(s[i])
                i = i + 1
                
            for k in range(temp):
                strr = strr + chrr
        else:
            chrr = s[i]
            i = i + 1
  
    return strr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    str_1 = DECRYPT(s)

    fptr.write(str_1 + '\n')

    fptr.close()
