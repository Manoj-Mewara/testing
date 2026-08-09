s1 = int(input("Enter the 1st Subject Marks: "))
s2 = int(input("Enter the 2nd Subject Marks: "))
s3 = int(input("Enter the 3rd Subject Marks: "))
Total = s1 + s2 + s3
Percentage = (Total/300)*100

if Percentage >= 90:
    print("A1 Grade")
elif Percentage >= 80:
    print("A2 Grade")
elif Percentage >= 70:
    print("B1 Grade")
elif Percentage >= 60:
    print("B2 Grade")
elif Percentage >= 50:
    print("C1 Grade")
elif Percentage >= 40:
    print("C2 Grade") 
else:
    print("Fail")

print("Total Marks:", Total)
print("Percentage:", Percentage)