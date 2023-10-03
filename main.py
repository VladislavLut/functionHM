def print_even_numbers(start, end):


    if start % 2 == 1:
        start == 1


    for number in range(start, end + 1):

        if number % 2 == 0:
            print(number)

print_even_numbers(2,10)