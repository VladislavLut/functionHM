def print_square(side_length, symbol, filled):

    for row in range(side_length):
        for column in range(side_length):
            if filled:
                print(symbol, end="")
            else:
                print("", end="")
    print()

print_square (5, "*", True)
