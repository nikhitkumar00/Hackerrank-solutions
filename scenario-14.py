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