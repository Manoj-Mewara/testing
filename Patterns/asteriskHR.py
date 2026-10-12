n = int(input("Enter a number of Row: "))
for i in range(n, 0, -1):                   #Bcz, we want to print reverse triangle. so our step size is -1. so loop can be run.
    for j in range(1, i + 1):
        print("*", end = " ")
    print()