"""
    A food court facilitates their customers with a featured app,
    where the customers can view the Menu Card and place their order.
    The order may be delivered on-premises as per policies.
    Write a code to take the order from the customers by pressing
    Menu: Item Number
    Quantity
    After one customer completes the process of placing the order by pressing the Menu: Item Number and Quantity, your code should accept 'Y' or 'y' to continue taking order or 'N' or 'n' for stopping the process of order taking.
    Final output should be the calculated Total Amount.
    Menu Card is given as:

    NUMBER          NAME                            PRICE
    ---------------------------------------------------------------
    1               Veg. Sandwich                   80.0
    2               Cheese Sandwich                 130.0
    3               Veg. Grill Sandwich             100.0
    4               Sada Dosa                       80.0
    5               Masala Dosa                     90.0
    6               Onion Rava Dosa                 110.0
    7               Onion Rava Masala Dosa          120.0
    8               Special Thattu Dosa             140.0
    9               Plain Uttapam                   70.0
    10              Onion Uttapam                   80.0
    ---------------------------------------------------------------

    You can use any suitable data structure to hold the Menu Card item's price.

    Input Format

        Input for Menu: Item Number should be an integer greater than 0 and less than 11.
        Input for Quantity should be an integer greater than 0 and less than 21.
        For any other input display "Invalid Input".
        
    EXAMPLE:

    Input:
        1 //For enter menu number
        2 //For enter quantity
        Y //Do you want to order more items?
        2 //For enter menu number
        3 //For enter quantity
        N //Do you want to order more items?

    Output:
        Total Amount: 550.0 INR

    Note:
        Input prompt should not be part of code
        (only accept values as input in the order as given above)

    Output Format
        For any invalid input, print:
        "Invalid Input"
        For all valid inputs you have to display total amount in the following format:
        Total Amount: x INR

    Sample Input 0
        1
        2
        Y
        2
        3
        N

    Sample Output 0
        Total Amount: 550.0 INR

    Sample Input 1
        1
        2
        Y
        2
        3
        Z

    Sample Output 1
        Invalid Input

    Sample Input 2
        11
        2
        Y
        2
        3
        N

    Sample Output 2
        Invalid Input
"""

total = 0
menu = {
    1:80,
    2:130,
    3:100,
    4:80,
    5:90,
    6:110,
    7:120,
    8:140,
    9:70,
    10:80
}
try:
    while(1):
        number = int(input())

        assert number > 0 and number < 11
        quantity = int(input())

        assert quantity > 0 and quantity < 21
        total += menu[number]*quantity
        more = input().upper()

        assert more == "Y" or more == "N"
        if more == "N":
            break
    
    print(f"Total Amount: {total}.0 INR")
except:
    print("Invalid Input")