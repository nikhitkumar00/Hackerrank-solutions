"""
    https://www.hackerrank.com/contests/manifold-7h9k0d/challenges/infix-to-prefix-2
"""

def islessprecedence(p, q):
    dict = {")": 0, "=": 1, "+": 2, "-": 2, "*": 3, "/": 3, "^": 4}     # ( for postfix
    a = dict[p]
    b = dict[q]

    if p == "^" and q == "^":
        return True     # False for postfix
    elif a < b:     # <= for postfix
        return True
    else:
        return False

def infixtoprefix(s):
    s = s[::-1]     # no need for postfix
    stack = []
    out = ""

    for ele in s:
        if ele.isalpha():
            out += ele
        elif ele == ")":     # ( for postfix
            stack.append(ele)
        elif ele == "(":     # ) for postfix
            while stack[-1] != ")":     # ( for postfix
                out += stack.pop()
            stack.pop()
        else:
            if ele not in "+-*/^":
                return "INVALID OPERATOR"
            else:
                while stack and islessprecedence(ele, stack[-1]):
                    out += stack.pop()
                stack.append(ele)
    while stack:
        out += stack.pop()

    return out[::-1]     # out for postfix


print(infixtoprefix("a+b-c^d^e"))
print(infixtoprefix("A+(B*C)-D/E"))
print(infixtoprefix("A+B*(C-D)*E^F^G"))
print(infixtoprefix("A+B*(C-D)*E^F@G"))
