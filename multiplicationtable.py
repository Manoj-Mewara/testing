n = int(input("Enter a Number: "))
for i in range(1, n + 1):
    for j in range(1, 11):
        print(i, "X", j, "=", i * j)
    # for spacing a line between the table, so we can print empty space. but write in the 1st for's indentation area. bcz, 1st for is refer to the print the number of given integer in loop one by one.
    print()     # it is spacing for a new line in between the table.

# print("\n")     it is spacing 2 lines. bcz of \n for one & () for onther one.

