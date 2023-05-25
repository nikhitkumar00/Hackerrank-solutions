"""
    Write code for finding the peak elements in an integer array.
    A peak element is the one which is not smaller than its left and right neighboring values.
    ie. arr[i-1] <= arr[i] => arr[i+1], arr[i] is a peak element.
    First and Last elements of the array may also be a peak element.
    For the last and first element only one comparison is needed. 
    An array may have more than one peak element. You have to find all of them.
    Input Format

    Input the size N of the integer array in line 1.
    Input all elements of the array each separated by a newline.

    Constraints
                N > 1

    Output Format

                Print all peak elements in the order of its occurance with a space between them.

    Sample Input 0

                5
                100 
                20 
                100 
                40 
                50 

    Sample Output 0

                100 100 50

    Sample Input 1

                5
                10 
                20 
                30 
                40 
                50

    Sample Output 1
    
                50
"""


n = int(input())
if n > 1:
    l = [int(input()) for i in range(n)]
    for i in range(len(l)):
        if i == 0:
            if l[0] >= l[1]:
                print(l[0], end=' ')
        elif i == len(l)-1:
            if l[len(l)-1] >= l[len(l)-2]:
                print(l[len(l)-1], end=' ')
        else:
            if l[i] >= l[i-1] and l[i] >= l[i+1]:
                print(l[i], end=' ')
