#!/bin/python3

import math
import os
import random
import re
import sys

def BIN_SEARCH(n, arr, key):
    z = _BIN_SEARCH(0, n-1, arr, key)
    return z

def _BIN_SEARCH(low, high, arr, key):
    l = low
    h = high
    while l <= h:
        m = (l + h)//2
        if key == arr[m]:
            return m
        elif key < arr[m]:
            return _BIN_SEARCH(l, m-1, arr, key)
        else:
            return _BIN_SEARCH(m+1, h, arr, key)
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    k = int(input().strip())

    idx = BIN_SEARCH(n, arr, k)

    fptr.write(str(idx) + '\n')

    fptr.close()
