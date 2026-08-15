n = int(input("Enter a Number: "))
s = 0   # it's stand for sum.
while n > 0:        # the logic is to run the loop until the number becomes 0.
    d = n % 10      # the logic is to get the last digit of the number by taking the modulus of 10.
    s = s + d       # the logic is to add the last digit to the sum.
    n = n // 10     # the logic is to remove the last digit from the number.
print("The sum of the digits is", s)

'''
If the number was negative, we handle it BEFORE the loop starts:

if n < 0:
    n = -n          # Pura number positive ho gaya

while n > 0:        # Ab positive hone ke baad yahan aayega
    # same code hereafter.
'''