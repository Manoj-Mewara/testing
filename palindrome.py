n = int(input("Enter a Number: "))
r = 0
p = n                                       # backup value for n, bcz of while loop.
while n > 0:
    d = n % 10
    r = r * 10 + d                          # the revers number's code.
    n = n // 10
   
if p == r:                                  # comparison of p & r to check n is a palindrome number.
    print(p, "is a palindrome number")
else:
    print(p, "is not a palindrome number")
print(p, "is the reverse number of", r)

'''
# Yahan int() nahi lagaya, toh 121 bhi text hai aur NITIN bhi text hai
p = input("Enter a Word or Number: ") 

# Slicing Magic: [::-1] ka matlab hai string ko end se start tak ulta padho
r = p[::-1]         # where -1 is for check string from the last leteer.

if p == r:
    print(p, "is a palindrome")
else:
    print(p, "is not a palindrome")
'''

