n = int(input("Enter a number of row: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end = " ")       # Where chr is character function, it is changes number into ASCII Table.
    print()