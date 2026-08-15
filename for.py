for i in range(1, 20, 2):   # in range(start, stop, step) function, the start value is inclusive and the stop value is exclusive. The step value determines the increment between each number in the sequence.
    print(i + 1)  # printing the current number in the range plus 1.
    print("Hello")  # printing "Hello" after each number in the range.
    
name = 'Manoj Mewara'
for j in name:  # iterating over each character in the string 'name'.
    print(j)
    if j == 'M':  # checking if the current character is 'M'.
        print("Found M")  # if the character is 'M', print "Found M".

Girls = ["Jaanvi", "Lavina", "Palak"]
for girl in Girls:
    print(girl)           # iterating over each name in the list 'Girls' and printing it if you don't use nested loop.
    for k in girl:          # iterating over each character in the string 'girl'.
        print(k)    
    