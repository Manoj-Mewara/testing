n = int(input("Enter a Number: "))
s = 0
p = n
for i in range(1, n):
    if n % i == 0:                          # the logic is to find the factor of n.
        s = s + i                           # the logic is to find the sum for the factor of n.
if s == n:                                  # comparing s & n to check the perfect number.
    print(p, "is a perfect number")
else:
    print(p, "is not a perfect number")
print("The summation of the factor is", s)

''' For while loop,
n = int(input("Enter a Number: "))
s = 0
p = n
i = 1                               # Step 1: 'i' ko start kiya

while i < n:                        # Step 2: Loop ki condition lagayi
    if n % i == 0:                  
        s = s + i                   
    i = i + 1                       # Step 3: 'i' ko aage badhaya (1 se 2, 2 se 3...)

# Baki ka check karne wala logic ekdum same rahega
if s == n:                                  
    print(p, "is a perfect number")
else:
    print(p, "is not a perfect number")
print("The summation of the factor is", s)
'''



