for i in range(11):
    if i == 4:
        break   # breaks the loop when i equals 4, exiting the loop entirely.
    print("5 x", i + 1, "=", 5 * (i + 1)) 

for i in range(11):
    if i == 4:
        continue    # continues to the next iteration of the loop when i equals 4, skipping the print statement for that iteration.  
    print("5 x", i, "=", 5 * i)

