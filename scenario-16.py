"""
    At a fun fair, a street vendor is selling different colours of balloons.
    He sells N number of different colours of balloons (B[]).
    The task is to find the colour of the balloons which is present odd number
    of times in the bunch of balloons.

    Note :
        If there is more than one colour which is odd in number,
        then the first colour in the array which is present odd number
        of times is displayed. The colours of the balloons can be either
        upper case or lower case in the array. If all the inputs are even
        in number, display the message “All are even”.

    Example 1 :

    Input :
        7 → Value of N
        [r, g, b, b, g, y, y] → B[]; Elements B[0] to B[N-1], where each input element is separated by new line.

    Output :
        r → “r” colour balloon is present odd number of times in the bunch.

    Explanation:
        From the input array above:
        r: 1 balloon
        g: 2 balloons
        b: 2 balloons
        y : 2 balloons
        Hence , r is only the balloon which is odd in number.

    Example 2 :

    Input :
        10 → Value of N
        [a, b, B, b, c, c, c, a, f, c] → B[]; Elements B[0] to B[N-1], where each input element is separated by new line.

    Output :
        b → “b” colour balloon is present odd number of times in the bunch.

    Explanation:
        From the input array above:
        a: 2 balloon
        b: 3 balloons
        c: 4 balloons
        f: 1 balloon
        Here, both ‘b’ and ‘f’ have odd number of balloons.
        But ‘b’ colour balloon occurs first.
        Hence , b is the output.

    Input Format
        First input: Accept value for number of N(Positive integer number).
        Second Input : Accept N number of character values(B[]),
                        where each value is separated by a new line.

    Constraints
        3<=N<=50
        B[i]={{a-z} or {A-Z}}

    Output Format
        The output should be a single literal(Check the output in Example 1 and Example 2).
        Incase of any constraint violation print "Invalid Input".

    Sample Input 0
        7
        r
        g
        b
        b
        g
        y
        y

    Sample Output 0
        r

    Sample Input 1
        10
        a
        b
        b
        b
        c
        c
        c
        a
        f
        c

    Sample Output 1
        b

    Sample Input 2
        3
        r
        g
        b

    Sample Output 2
        r
"""

try:
    n = int(input())
    list=[]

    assert n >= 3 and n <=50

    for i in range(n):
        temp = input().lower()
        assert temp.isalpha()
        assert len(temp) == 1
        list.append(temp)

    for i in list:
        if list.count(i) % 2 != 0:
            print(i)
            break
    else:
        print("All are even")
except:
    print("Invalid Input")