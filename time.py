import time
current_time = time.strftime('%H')
Wishing = int(current_time)             # if i don't convert it to int, it will be string. but the program also can run. but, we write in "" or '' . & enter the 2 digit number like 04, 24 etc. because we use the time.strftime() method. so do it.
if Wishing >= 5 and Wishing < 12:
    print("Good morning!")
elif Wishing >= 12 and Wishing < 18:
    print("Good afternoon!")
elif Wishing >= 18 and Wishing < 21:
    print("Good evening!")
elif Wishing >= 21 or Wishing < 5:     # i also can use else. 
    print("Good night!")
print("The current time is:", current_time)


