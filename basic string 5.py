"""
Two strings X and Y are called isomorphic strings if all the occurrences of each character in X can be replaced with another character to get Y and vice-verca.
For example, consider the strings "ACAB" and "XCXY". They are isomorphic as we can map 'A'->'X', 'B'->'Y', and 'C'->'C'
Note that mapping from a character to itself is allowed but no two characters may be replaced by the same character.

Input Format

Two strings, X and Y are already taken as inputs and given as input parameters in the function.
You are not supposed to take any inputs.

Constraints

NA

Output Format

Return "YES" if the strings X and Y are isomorphic, otherwise return "NO".

Sample Input 0

ACAB
XCXY
Sample Output 0

YES
Sample Input 1

egg
add
Sample Output 1

YES
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def ISOMORPHIC(X, Y):
    dict_pair = {}
    if len(X) != len(Y):
        return "NO"
    for i in range(len(X)):
        if X[i] not in dict_pair:
            dict_pair[X[i]] = Y
        elif dict_pair[X[i]] != Y:
            return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = input()

    Y = input()

    Z = ISOMORPHIC(X, Y)

    fptr.write(Z + '\n')

    fptr.close()
