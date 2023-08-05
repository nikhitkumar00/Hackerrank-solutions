"""
    Jack is always excited about sunday. It is his favourite day,
    which he gets to play all day and goes to cycling with his friends.
    So every time when the month starts he counts the number of sundays
    he will get to enjoy. Considering the month can start with any day,
    be it Sunday, Monday… or so on. If the day starts with Sunday, that
    Sunday is also considered.
    Count the number of Sundays jack will get within n number of days.

    Example :

    Input :
        mon → input string(lower case) denoting the start day of the month.
        13 → input integer denoting the number of days from the start day of the month.

    Output :
        1 → number of Sundays within 13 days.

    Explanation:
        The month start with mon(Monday). So the upcoming sunday will arrive in next 6 days and the next Sunday in next 7 days and so on. Now total number of days are 13. It means 6 days to first sunday and then remaining 6 days won't end up in another sunday. Total 1 sunday may fall within 13 days.

    Input Format
        Get an input string(lower case) denoting the start day of the month in the first line.
        Get an input integer denoting the number of days from the start day of the month in the second line.

    Constraints
        Input string should be in lower case and and it should be the first 3 letters of days.
        No. of days(d) from the start of month should be greater than 0, ie; d>0.

    Output Format
        Print the count of Sundays as output and if the input violates the constraint, print "Wrong Input"

    Sample Input 0
        mon
        13

    Sample Output 0
        1

    Sample Input 1
        Mon
        13

    Sample Output 1
        Wrong Input

    Sample Input 2
        sat
        30

    Sample Output 2
        5

    Sample Input 3
        mon
        14

    Sample Output 3
        2
"""

start = input()
count = 0
dict = {"sun":0,"mon":6,"tue":5,"wed":4,"thu":3,"fri":2,"sat":1}

if start in dict:
    numberofdays = int(input())

    if numberofdays > 0:
        numberofdays = numberofdays - dict[start]
        count += 1
        count += numberofdays//7 - 1

        if numberofdays % 7 != 0:
            count += 1

        print(count)
        
    else:
        print("Wrong Input")

else:
    print("Wrong Input") 