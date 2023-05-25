"""
A doctor has a clinic where he serves his patients. The doctor’s consultation fees are different for different groups of patients depending on their age. If the patient’s age is below 17, fees is 200 INR. If the patient’s age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR. Write a code to calculate earnings in a day for which one Array/List of values representing age of patients visited on that day is passed as input.
Age should not be zero or less than zero or above 120.
Doctor consults a maximum (max) of 20 patients a day.

Input Format

Enter all the age values one by one without a value to stop.

Constraints

max <= 20
0 < age <= 120

Output Format

Any wrong input may lead to print the message "Invalid Input".
For valid inputs, output the total income in the following format.
Total Income: X INR

Sample Input 0

20
30
40
50
2
3
14

Sample Output 0

Total Income: 2100 INR

Sample Input 1

16
17
40
41

Sample Output 1

Total Income: 1300 INR

"""

total = 0
count = 0

try:
    while count < 20:
        n = int(input())

        if n <= 0 or n >120:
            print("Invalid Input")
            exit()

        if n > 40:
            total += 300
        elif n > 16:
            total += 400
        else:
            total += 200
        count += 1
        if count > 20:
            print("Invalid Input")
    print("Total Income: "+str(total)+" INR")

except EOFError:
    print("Total Income: "+str(total)+" INR")