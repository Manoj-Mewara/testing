n = int(input("Enter a Number of Row: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")                    # the logic is to print 1 to given number one by one in column. like 1 2 3 ... & j refer for column.
    print() 

""" 
n = int(input("Enter a Number of Row: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end = " ")                    # the logic is to print same number in row. loke 3 3 3 ... & i refer for row .
    print() 
"""

'''
For j: # Logic: 'j' represents the column number. It resets to 1 for every new row and prints incrementally up to 'i'.

For i: # Logic: 'i' represents the current row number. It stays constant throughout the inner loop, repeating the same value.
'''