"""
            We have to estimate the cost of painting a property.
            Interior wall painting cost is Rs. 18 per sq.ft. 
            and exterior wall painting cost is Rs. 12 per sq.ft.
            If a user enters zero as the number of walls then skip surface area 
            values as user may don’t want to paint that wall and for any wrong input 
            print "Invalid Input".

            Input Format

            Take input as
            1. Number of interior walls 'n'
            2. Number of exterior walls 'm'
            3. Surface area of each interior wall in units of sq.ft.
            4. Surface area of each exterior wall in units of sq.ft.

            Constraints

            0 <= n <= 10
            0 <= m <= 10

            Output Format

            Calculate and display the total cost of, painting the property in the following format.
            Total Estimated Cost: X INR

            Sample Input 0      6
                                3
                                12.3
                                15.2
                                12.3
                                15.2
                                12.3
                                15.2
                                10.10
                                10.10
                                10.00

            Sample Output 0     Total Estimated Cost: 1847.4 INR

            Sample Input 1      0
                                0

            Sample Output 1     Total Estimated Cost: 0.0 INR
"""

n = int(input())
m = int(input())
if 0 <= n <= 10 and 0 <= m <= 10:
    cost = 0
    for i in range(n):
        temp = float(input())
        cost = cost + (temp*18)
    for i in range(m):
        temp = float(input())
        cost = cost + (temp*12)
    print(f"Total Estimated Cost: {cost:.1f} INR")
else:
    print("Invalid Input")
