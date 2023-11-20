def print_diamond(rows):
    i = 1
    while i <= rows:
        print(" " * (rows - i), end="")
        print("*" * (2 * i - 1))
        i += 1
    i = rows - 1
    while i > 0:
        print(" " * (rows - i), end="")
        print("*" * (2 * i - 1))
        i -= 1

rows = 5  # Change the number of rows as needed
print_diamond(rows)


