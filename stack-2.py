def Push(stack, data):
    stack.append(data)
    return "PUSHED SUCCESSFULLY"

def Pop(stack):
    if stack:
        return str(stack.pop())
    else:
        return "STACK UNDERFLOW"

def isEmpty(stack):
    if stack:
        return False
    else:
        return True

def Peek(stack):
    if stack:
        return str(stack[-1])
    else:
        return "STACK UNDERFLOW"