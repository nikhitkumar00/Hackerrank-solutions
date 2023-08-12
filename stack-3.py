"""
    https://www.hackerrank.com/contests/manifold-7h9k0d/challenges/basic-dsa-2
"""

def isBalanced(expr):
    str = expr.replace(" ","")
    stack = []
    try:
        for ele in str:
            if ele in "{[(":
                stack.append(ele)
            else:
                if ele == "}":
                    assert stack[-1] == "{"
                    stack.pop()
                elif ele == "]":
                    assert stack[-1] == "["
                    stack.pop()
                elif ele == ")":
                    assert stack[-1] == "("
                    stack.pop()
        else:
            return "BALANCED"
    except:
        return "NOT BALANCED"

print(isBalanced("){(){}[]}("))
print(isBalanced("( ( { } [ ] ) { { } } )"))
print(isBalanced("({[]{{}})"))
print(isBalanced("{ } } { { }"))