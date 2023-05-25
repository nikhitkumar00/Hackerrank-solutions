"""
Take a single line text message from the user. Separate the vowels from the text and display count of each vowel's occurrences in the lexicographic order. Remove all the vowels from the given input text and display that text in the next line.
Display the output in the exact format shown below, as shown in the sample test case.

Input Format

Input a string

Constraints

NA

Output Format

If the text message entered by the user doesn't contain any vowels, then display "0" as output.
If the text message entered by the user contain any character other than alphabet or space, then display "Invalid Input" as output.
"Invalid Input" is case sensitive, display it in the exact format given.

Sample Input 0

Hello Welcome

Sample Output 0

a:0
e:3
i:0
o:2
u:0
Hll Wlcm

Sample Input 1

Hll Wlcm

Sample Output 1

0

"""

s = input()
a = 0
e = 0
i = 0
o = 0
u = 0
total = 0

for k in s:
    if k.isalpha() == 1 or k == ' ':
        if k in 'aA':
            a += 1
            total += 1
        if k in 'eE':
            e += 1
            total += 1
        if k in 'iI':
            i += 1
            total += 1
        if k in 'oO':
            o += 1
            total += 1
        if k in 'uU':
            u += 1
            total += 1
    else:
        print("Invalid Input")
        exit()

if total != 0:
    print('a:'+str(a))
    print('e:'+str(e))
    print('i:'+str(i))
    print('o:'+str(o))
    print('u:'+str(u))

    vowels = 'AEIOUaeiou'
    for i in s:
        if i not in vowels:
            print(i, end='')
else:
    print('0')
