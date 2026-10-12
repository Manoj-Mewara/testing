"""
n = int(input("Enter a number of row: "))
c = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        c += 1
        if c % 2 == 0:
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()
"""
n = int(input("Enter a number of row: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        
        # Seedha i aur j ka total check karo
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
            
    print()
