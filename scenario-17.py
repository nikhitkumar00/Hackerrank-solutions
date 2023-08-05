try:
    price = {1:50,2:100,3:40,4:200,5:300}
    n = int(input())
    itemno = list(map(int,input().split()))
    assert itemno in price
    quantity = list(map(int,input().split()))

except:
    print("INVALID INPUT")