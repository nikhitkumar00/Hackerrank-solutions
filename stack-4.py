s = "a+b*(c-d+e)/f*(g-h/i)"
stack = []
out = ""


def islessprecedence(p, q):
    dict = {"(": 0, "=": 1, "+": 2, "-": 2, "*": 3, "/": 3, "^": 4}
    a = dict[p]
    b = dict[q]

    if p=="^" and q =="^":
        return False
    elif a <=b:
        return True
    else:
        return False
    
for ele in s:
    if ele.isalpha():
        out += ele
    elif ele == "(":
        stack.push(ele)
    elif ele == ")":
        