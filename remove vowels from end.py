s = "abcdaeiou"
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
while 1:
    if len(s) != 0 and s[-1] in vowels:
        s = s[:-1]
    else:
        break
print(s)
