def is_pollindrome(number):

    number_string = str(number)

    first_half = number_string[:len(number_string) // 2]
    second_half = number_string[len(number_string) // 2:][::-1]

    return first_half == second_half
print(is_pollindrome(123321))