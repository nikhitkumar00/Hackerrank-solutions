"""
			Write code for finding the sum of the series given below
			after accepting the value of 'N' as input.
			S = 1 + (1+2) + (1+2+3) + (1+2+3+4) + .......+ (1+2+3+.......N)
"""

n = int(input())
total = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        total = total + j

print(total)
