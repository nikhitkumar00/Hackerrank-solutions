"""
    https://www.hackerrank.com/contests/manifold-7h9k0d/challenges/stack-06
"""


def prefix(s):
    s = s.split()
    s.reverse()
    stack = []

    for ele in s:
        if ele.isdigit():
            stack.append(ele)
        elif ele in "+-*/^":
            op1 = float(stack.pop())
            op2 = float(stack.pop())

            if ele == "+":
                stack.append(op1 + op2)
            elif ele == "-":
                stack.append(op1 - op2)
            elif ele == "*":
                stack.append(op1 * op2)
            elif ele == "/":
                stack.append(op1 / op2)
            elif ele == "^":
                stack.append(op1 ** op2)
        else:
            return -99999
    return stack.pop()

print(prefix("+ 10 * / 100 50 15"))
print(prefix("- + 1000 500 ^ 2 ^ 3 2"))
print(prefix("+ 5 * * 10 - 200 100 ^ 2 ^ 3 2"))