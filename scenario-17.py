try:
    price = [50,100,40,200,300]
    n = int(input())
    total = 0
    itemno = list(map(int,input().split()))
    quantity = list(map(float,input().split()))

    for i in range(len(itemno)):
        total += price[itemno[i]-1] * quantity[i]
    
    if total >= 1000:
        total -= total * 0.1
    
    if input().lower() == "y":
        total -= total * 0.05
    
    print(f"{total} INR")

except:
    print("INVALID INPUT")