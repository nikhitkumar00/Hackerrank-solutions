"""
    A customer has a choice to buy TV from set of 3 company models provided by the store.
    If customer takes an exchange offer,then customer will get a discount of 2%,
    if the old TV is not working else he will get a discount of 20%.
    If the customer do not opt for exchange offer then,
    he has to pay MRP of the TV and display that amount.
    Menu for TV condition should be displayed only if customer choose for exchange offer.
    Whenever the user enters an invalid option,
    then the code should stop with message "Invalid Input" and
    it should be displayed in the same format as it is case sensitive.
    Assume the following list is already seen by the customer.
    There should be 3 inputs for each customer,
    whose answer should be a number given with that choice.

    FIRST INPUT CHOICE:
    Display List(Select TV Model)
    1. Samsung 10000 RS
    2. Onida 7000 RS
    3. HDLC 6000 RS

    SECOND INPUT CHOICE:
    Want To Take Exchange Offer?
    1. Yes
    2. No

    THIRD INPUT CHOICE:
    Current Condition Of Customer's Old TV
    1. Working
    2. Not Working

    Input Format
    For example, if the customer want HDLC TV and if he opt for exchange offer for his old TV which is in working condition, then the output will be 4800.00 INR.
    All input values should be entered in the following format.
    3
    1
    1
    Note that when the customer do not opt for exchange offer, there will be only 2 inputs.

    Constraints
    NA

    Output Format
    For all invalid inputs, output will be
    Invalid Input

    For all valid inputs, output will be
    x INR (Where x is the amount customer has to pay rounding off to two digts after the decimal point)

    Sample Input 0
    3
    1
    1

    Sample Output 0
    4800.00 INR

    Sample Input 1
    3
    2
    1

    Sample Output 1
    6000.00 INR
"""

model = input()
try:
    model = int(model)
    
    if model in [1, 2, 3]:
        if model == 1:
            price = 10000
        elif model == 2:
            price = 7000
        else:
            price = 6000
        
        exchange = input()
        exchange = int(exchange)

        if exchange == 1:
            working = input()
            working = int(working)

            if working == 1:
                total = price - (price * 0.2)
            elif working == 2:
                total = price - (price * 0.02)
            else:
                exit()

        elif exchange == 2:
            total = price
        else:
            exit()

        print(f"{total:.2f} INR")
            
    else:
        exit()
        
except:
    print("Invalid Input")