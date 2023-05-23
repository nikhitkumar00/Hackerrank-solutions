"""
Given an array arr[] of n elements sorted in increasing order, write a code for searching the given element 'x' in arr[].
A simple approach is to do linear search.The time complexity of above algorithm is O(n).
Another approach to perform the same task is using Binary Search.
Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log n).
Use are supposed to use binary search for getting the solution of this problem.

Input Format

Size of the array and key to be searched are given as input parameters of the function in that order.
You are not supposed to take any input.

Constraints

NA

Output Format

If the element is present in the array, return the index of the array element 'x'.
If the element is not present in the array, return '-1'.

Sample Input 0

5
10 20 30 40 50
50
Sample Output 0

4
Sample Input 1

10
100 200 300 400 500 600 700 800 900 1000
100
Sample Output 1

0
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def BIN_SEARCH(n, arr, key):
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid-1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    k = int(input().strip())

    idx = BIN_SEARCH(n, arr, k)

    fptr.write(str(idx) + '\n')

    fptr.close()
