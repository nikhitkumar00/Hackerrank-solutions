"""
    Given an integer array Arr of size N, the task is to find the count
    of elements whose value is greater than all of its prior elements.
    Note :
    1st element of the array should always be considered in the count of the result.
    For example, Arr[]={7, 4, 8, 2, 9}
    As 7 is the first element, it will consider in the result.
    8 and 9 are also the elements that are greater than all of
    its previous elements. Here, a total of 3 elements is present
    in the array that meets the condition.
    Hence the output = 3.
    Expected Time complexity is O(n) and Auxiliary Space Complexity is O(1).

    Example 1 :

    Input :
        5 → Value of N, represents size of Arr
        7 → Value of Arr[0]
        4 → Value of Arr[1]
        8 → Value of Arr[2]
        2 → Value of Arr[3]
        9 → Value of Arr[4]

    Output :
        3

    Example 2 :

    Input :
        5 → Value of N, represents size of Arr
        3 → Value of Arr[0]
        4 → Value of Arr[1]
        5 → Value of Arr[2]
        8 → Value of Arr[3]
        9 → Value of Arr[4]

    Output :
        5

    Input Format
        NA

    Constraints
        1<=N<=20
        0<=Arr[i]<=10000

    Output Format
        NA

    Sample Input 0
        5
        7
        4
        8
        2
        9

    Sample Output 0
        3

    Sample Input 1
        5
        3
        4
        5
        8
        9

    Sample Output 1
        5
"""

n = int(input())
l = [int(input()) for i in range(n)]
count = 0
max = -1

for i in range (n):
    if l[i] > max:
        max = l[i]
        count += 1
print(count)