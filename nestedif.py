n = int(input("Enter a Number: "))

if n < 0:
    print("Negative Number")
elif n > 0:
    if n % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Zero")
print("Number is:", n)

# Conditional Operators:
# (i)     <     : Less than
# (ii)    >     : Greater than
# (iii)   <=    : Less than or equal to
# (iv)    >=    : Greater than or equal to
# (v)     ==    : Equal to
# (vi)    !=    : Not equal to
