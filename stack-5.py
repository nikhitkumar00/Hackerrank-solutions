"""
    https://www.hackerrank.com/contests/manifold-7h9k0d/challenges/basic-dsa-4/problem
"""

def postfix(str):
    list = str.split()
    stack = []

    for term in list:
        if term.isdigit():
            stack.append(term)
        elif term in "+-*/^":
            op2 = float(stack.pop())
            op1 = float(stack.pop())
            if term == "^":
                stack.append(op1**op2)
            elif term == "*":
                stack.append(op1*op2)
            elif term == "/":
                stack.append(op1/op2)
            elif term == "+":
                stack.append(op1+op2)
            elif term == "-":
                stack.append(op1-op2)
        else:
            return -99999
    return(stack.pop())

print(postfix("10 100 50 / 15 * +"))
print(postfix("10 22 - 8 / 6 * 5 +"))
print(postfix("10 20 30 10 - / 2 2  2 ^ ^ * +"))
print(postfix("10 20 30 10 - / 2 2  2 ^ ^ * $"))