"""
A string or character array represents a mobile no. and an array containing five mobile numbers is provided. Verify these five mobile numbers and identify valid and invalid mobile numbers.
Any mobile number which have more or less than 10 digits is considered as invalid. Write a code which will generate a report on the count of total number of valid mobile numbers.
A valid mobile no. 'M' should be of length 10 with all numeric digits.

Input Format

Do not use any input message. Directly accept mobile numbers one after another as input and enter 'Q' or 'q' to stop taking input.

Constraints

NA

Output Format

Output should be an integer no. which represents the count of valid mobile numbers.
If a user enters a set of mobile numbers containing less than or more than 5, display the below given message and quit:
"INPUT LIMIT IS 5"

Sample Input 0

9867549879
989A367378
9892568790
9898767a88
98989856745
Q
Sample Output 0

2
Sample Input 1

6743245663
7567686533
35577g2466
25o5353363
q
Sample Output 1

INPUT LIMIT IS 5
"""

l = []
flag = 0

while(1):
    n = input()

    if n == 'q' or n == 'Q':
        if len(l) != 5:
            print("INPUT LIMIT IS 5")
            exit()
        break
        
    elif len(l) > 5:
        print("INPUT LIMIT IS 5")
        exit()
    
    l.append(n)
    if len(n) != 10:
        flag = flag + 1
        continue

    for c in n:
        if c.isdigit() == 0:
            flag = flag + 1
            break
            
print(len(l)-flag)