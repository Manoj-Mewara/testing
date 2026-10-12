# i = rows & j = columns

n = int(input("Enter a Number of Row: "))
num = 1                                     # the number's pattern starts from 1.
for i in range(1, n+1):   
    for j in range(1, i + 1):
        print(num, end = " ")               # the logic is to print num column one by one with one space _ .
        num += 1                            # with increament of 1.
    print()                                 # if inner loop ends, so next one print in new line.