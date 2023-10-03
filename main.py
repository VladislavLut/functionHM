def find_min(a, b, c, d, e):

    min_number = a
    if b < min_number:
        min_number = b
    if c < min_number:
        min_number = d
    if e < min_number:
        min_number = e

    return min_number

print(find_min(1, 2, 3, 4, 5))