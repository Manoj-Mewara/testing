n = int(input("Enter a Number: "))
p = n
c = 0
for i in range(2, n):                           # this not include 1 & n
    if n % i == 0:                              # find the factor of n
        c = c + 1                                # count the factor of n
        break
if c == 0:
    print(p, "is a Prime Number")
else:
    print(p, "is not a Prime Number")

""" It is only for practise.
prime_count = 0
for j in range(2, n + 1):
    if n % j != 0:
        prime_count += 1
        print(j)
print("The total prime number between 2 and", p, "are", prime_count)
"""

