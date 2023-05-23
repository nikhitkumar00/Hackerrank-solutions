import math
import os
import random
import re
import sys

def FREQ(L):
    dict1 = dict.fromkeys(L,0)

    for ele in L:
        dict1[ele] = dict1[ele] + 1
    for key in dict1:
        print(key,dict1[key])

if __name__ == '__main__':
    n = int(input().strip())

    L = list(map(int, input().rstrip().split()))

    FREQ(L)
import math
import os
import random
import re
import sys

def FREQ(L):
    dict1 = dict.fromkeys(L,0)

    for ele in L:
        dict1[ele] = dict1[ele] + 1
    for key in dict1:
        print(key,dict1[key])

if __name__ == '__main__':
    n = int(input().strip())

    L = list(map(int, input().rstrip().split()))

    FREQ(L)
