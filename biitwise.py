a = 3
b = 2
c = 1

d = a | b & c
print(d)

d = a | b & ~c
print(d)

"""
    Precedence (Decreasing)
    ~   Negation
    &   And
    |   Or
"""