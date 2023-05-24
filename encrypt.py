def ENCRYPT(s):
    chrr = ''
    oldchrr = ''
    count = 1
    strr = ''

    for i in range(1,len(s)):
        chrr = s[i]
        oldchrr = s[i-1]
        if chrr == oldchrr:
            count = count + 1
        else:
            strr = strr + oldchrr + str(count)
            count = 1
    return strr

s = 'aabaacddeeeeeeeeeeff'
print(ENCRYPT(s))