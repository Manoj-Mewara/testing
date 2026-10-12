n = int(input("Enter a Number: "))
r = len(str(n))                             # 1st we convert int into str. so, we can make the len of n's variable
s = 0
a = n
while n > 0:
    d = n % 10
    s = s + d**r                            # the generalize formula for armstrong number.
    n = n // 10
if s == a:
    print(a, "is an Armstrong Number")
else:
    print(a, "is not an Armstrong Number")
    
print("The summation of", a, "is", s)
