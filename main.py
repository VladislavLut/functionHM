def find_product(start, end):

    if start > end:
        start, end = end, start

    product = 1
    for number in range(start, end + 1):
        product *= number
    return product
print(find_product(2,5))