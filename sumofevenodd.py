def sumOfEvenOdd(num):

    sume = 0
    sumo = 0
    while (num > 0):
        if ((num % 10) % 2 == 0):
            sume += (num % 10)
        else:
            sumo += (num % 10)
        num = num//10
    return (sume, sumo)


def main():
    x = sumOfEvenOdd(1234)
    print(x)


if __name__ == "__main__":
    main()
