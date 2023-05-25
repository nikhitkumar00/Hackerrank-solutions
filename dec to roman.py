def DEC_ROM(n):
    symbols = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]

    roman = ""

    for symbol, value in symbols:
        while n >= value:
            roman += symbol
            n -= value

    return roman


print(DEC_ROM(int(input())))
