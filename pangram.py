"""
    A sentence having all the alphabets is known as pangram
"""

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "abcdefghijklmnopqrstuvwxyz"

str1 = str1.replace(" ","")
str1 = str1.lower()

l = sorted(set(str1))

new = ""

for i in l:
    new = new + i
    
if new == str2:
    print("Pangram")
else:
    print("Not Pangram")