"""
    FULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just a press of button.
    A vending machine can serve range of products as follows:

    Coffee
    1.Espresso Coffee
    2.Cappuccino Coffee
    3.Latte Coffee

    Tea
    1.Plain Tea
    2.Assam Tea
    3.Ginger Tea
    4.Cardamom Tea
    5.Masala Tea
    6.Lemon Tea
    7.Green Tea
    8.Organic Darjeeling Tea

    Soups
    1.Hot and Sour Soup
    2.Veg Corn Soup
    3.Tomato Soup
    4.Spicy Tomato Soup

    Beverages
    1.Hot Chocolate Drink
    2.Badam Drink
    3.Badam-Pista Drink

    Write a program to take input for main menu & sub menu and
    display the name of sub menu selected in the format given below.

    Input Format
        Input first letter(not case sensitive) to select main menu.
        Input the number corresponding to sub menu.

    Constraints
        No Constraint

    Output Format
        For any wrong input display:
        INVALID INPUT
        otherwise display:
        WELCOME TO CCD!
        Enjoy your x..(selected submenu item)

    Sample Input 0
        c
        1

    Sample Output 0
        WELCOME TO CCD!
        Enjoy your Espresso Coffee..

    Sample Input 1
        t
        9

    Sample Output 1
        INVALID INPUT
"""

items = [
    ["Espresso Coffee","Cappuccino Coffee","Latte Coffee"],
    ["Plain Tea","Assam Tea","Ginger Tea","Cardamom Tea","Masala Tea","Lemon Tea","Green Tea","Organic Darjeeling Tea"],
    ["Hot and Sour Soup","Veg Corn Soup","Tomato Soup","Spicy Tomato Soup"],
    ["Hot Chocolate Drink","Badam Drink","Badam-Pista Drink"]
]
search = ["c","t","s","b"]
try:
    item = input().lower()
    assert item in search
    choice = int(input())
    str = items[search.index(item)][choice-1]
    print(f"WELCOME TO CCD!\nEnjoy your {str}..")

except:
    print("INVALID INPUT")