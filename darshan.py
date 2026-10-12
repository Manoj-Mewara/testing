# Program for prime number checking
n = int(input("Enter a number: "))
p = n
c = 0
for i in range(2, n):  # this not include 1 & n
    if n % i == 0:  # find the factor of n
        c = c + 1  # count the factor of n
        break
if c == 0:
    print(p, "is a Prime Number")
else:
    print(p, "is not a Prime Number")



