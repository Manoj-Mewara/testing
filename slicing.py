Name = "Lavina"
Namelength = len(Name)
print("Her name's length is:", Namelength)
print(len(Name))
print(Name[:]) # prints the whole string
print(Name[:5]) # prints from the beginning to index 5 (exclusive)
print(Name[2:5]) # prints from index 2 to index 5 (exclusive)
print(Name[0:6]) # prints from the beginning to index 6 (exclusive), 0 but not 6
print(Name[0:6:2]) # prints from the beginning to index 6 (exclusive) with a step of 2
print(Name[-2:6]) # [len(Name)-2:6] prints from index 3 to index 6 (exclusive), means 3 but not 6
print(Name[-3:1]) # [len(Name)-3:1] prints from index 2 to index 1 (exclusive), means that's not make sense. so, it will print nothing. blank

