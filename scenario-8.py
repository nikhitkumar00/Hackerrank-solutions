"""
An English school teacher is teaching how to build sentences for kindergarten students. She starts by teaching two words in a sentence, then 3 words and so on. The next step is that she asks the students to find which word in the sentence they have made has the maximum number of alphabets. The task here is to write program to find the longest word in each input sentence(str).
Note :
The sentence can consist of uppercase, lowercase alphabets, special characters and numbers. Sentence need not end with a '.' symbol.

Example 1 :
Input :
Knowledge is the greatest gift → Input Sentence(String)

Output :
9 → Length of word with maximum characters.

Example 2 :
Input :
11223##%%5566778899 Saturn V rocket’s first stage carries 203,400 gallons (770,000 litres) of kerosene fuel → Input Sentence(String)

Output :
19 → Length of word with maximum characters.

Input Format

The candidate has to write the code to accept one input.
First Input : A sentence of words.

Constraints

str = A-Z, a-z, 0-9, special characters

Output Format

The output should be a positive integer number which represents the length of the longest word in the sentence.
If the input is an empty string print "Invalid Input".

Sample Input 0

Knowledge is the greatest gift

Sample Output 0

9

Sample Input 1

11223##%%5566778899 Saturn V rocket's first stage carries 203,400 gallons (770,000 litres) of kerosene fuel
Sample Output 1

19

"""

try:
    sentence = input().split()
    large = -1
    if len(sentence) == 0:
        print("Invalid Input")
        exit()

    for word in sentence:
        flag = len(word)
        if flag > large:
            large = flag
    print(large)
except EOFError:
    print("Invalid Input")