n = int(input("Enter a Number: "))
sum_even = 0
sum_odd = 0
even_count = 0
odd_count = 0
while n > 0:                            # the logic is to run the loop until the number becomes 0.
    d = n % 10                          # the logic is to get the last digit of the number by taking the modulus of 10.
    if d % 2 == 0:                      # the logic is to find even numbers.
        sum_even = sum_even + d         # the logic is add the digit for even summation else odd summation.
        even_count = even_count + 1     # the logic is, if it is even, so count + 1 else odd count + 1
        print(d, "is even")
    else:                               # the logic is to find non-even number, like odd.
        sum_odd = sum_odd + d
        odd_count = odd_count + 1
        print(d, "is odd")
    n = n // 10
print("The sum of even digits is", sum_even)
print("The sum of odd digits is", sum_odd)
print("The count of even digits is", even_count)
print("The count of odd digits is", odd_count)
