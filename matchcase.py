X = int(input("Enter the value of X: "))
match X:
    # match statement is used to compare the value of X with different cases.
    case 1:
        print("You entered one.")   
    case 2:
        print("You entered two.")
    case _ if X > 2:
        print("You entered a number greater than two.")
    case _:
        print("You entered a number less than one.\n", X, "is not a valid input.")
