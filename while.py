# if c = 5 so print the value of c until it reaches 0 
c = int(input("Enter the value of c: "))  # taking input from the user and converting it to an integer.
while c > 0:
    print(c)
    c = c - 1  # decrementing the value of c by 1 in each iteration of the while loop.
else:
    print("The value of c has reached 0.")  # printing a message when the while loop condition is no longer true.

# cc = 5            # infinte loop because the value of cc is always greater than 0 and it will never reach 0.
# while cc > 0:
#     print(cc)
#     cc = cc + 1  # incrementing the value of cc by 1 in each iteration of the while loop.

# do while loop in python is not available but we can use while loop to achieve the same functionality.
while True:  # Ye ek infinite loop hai, seedha andar ghusne dega
    n = int(input("Enter a positive number (0 to stop): "))
    print("You entered:", n)
    
    if n <= 0:  # Bahar nikalte waqt condition check ho rahi hai
        break   # Agar condition match hui, toh loop tod do