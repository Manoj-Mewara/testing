n = int(input("Enter a Number: "))
r = 0   # it's stand for reverse.
while n > 0:        # the logic is to run the loop until the number becomes 0.
    d = n % 10      # the logic is to get the last digit of the number by taking the modulus of 10.
    r = r * 10 + d  # the logic is to multiply the reverse number by 10 and add the last digit to it.
    n = n // 10     # the logic is to remove the last digit from the number by performing integer division by 10.
print("The reverse number is", r)

# The shortcut for the above code 
# print("The reverse number is", str(n)[::-1])  # This line reverses the number by converting it to a string, slicing it in reverse order, and converting it back to an integer.


