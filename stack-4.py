"""
    https://www.hackerrank.com/contests/manifold-7h9k0d/challenges/basic-dsa-3
"""


def infixtopostfix(s):
    stack = []
    out = ""

    def islessprecedence(p, q):
        dict = {"(": 0, "=": 1, "+": 2, "-": 2, "*": 3, "/": 3, "^": 4}
        a = dict[p]
        b = dict[q]

        if p == "^" and q == "^":
            return False
        elif a <= b:
            return True
        else:
            return False

    for ele in s:
        if ele.isalpha():
            out += ele
        elif ele == "(":
            stack.append(ele)
        elif ele == ")":
            while stack[-1] != "(":
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

    return out


print(infixtopostfix("a+b*c-d/e"))
print(infixtopostfix("a+b*(c-d+e)/f*(g-h/i)"))
print(infixtopostfix("a^b^c+d-e*(f+g/h)^i^j"))
print(infixtopostfix("a+b*(c-d+e)/f*(g-h&i)"))