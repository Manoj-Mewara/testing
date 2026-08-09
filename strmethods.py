# Strings are immutable in Python. This means that once a string is created, it cannot be changed. However, you can create new strings based on existing ones using various string methods.
a = 'ManoJ'
print(a.lower())
print(a.upper())
b = '  Manoj Mewara  '
print(b.strip()) # removes leading and trailing whitespace. but not the whitespace in between the string.    
c = 'Hi, Manoj!'
print(c.rstrip("!")) # removes trailing characters (in this case, the exclamation mark). but not the leading characters. but not the whitespace in between the string.
print(c.lstrip("Hi,")) # removes leading characters (in this case, "Hi,"). but not the trailing characters. but not the whitespace in between the string.
print(c.replace("Hi", "Bye")) # replaces occurrences of "Hi" with "Bye". but not the whitespace in between the string.
d = 'MTR Group'
print(d.split()) # splits the string into a list of words based on whitespace. but not the whitespace in between the string.
print(a.capitalize()) # capitalizes the first character of the string and makes all other characters lowercase. but not the whitespace in between the string.
print(d.center(20)) # centers the string within a specified width (20 in this case). but not the whitespace in between the string.
print(d.center(50, "*")) # centers the string within a specified width (50 in this case) and fills the extra space with asterisks. but not the whitespace in between the string.
print(b.count("M")) # counts the occurrences of "M" in the string. but not the whitespace in between the string.
print(c.endswith("!")) # checks if the string ends with "!" and returns True or False. but not the whitespace in between the string.
print(c.startswith("Hi")) # checks if the string starts with "Hi" and returns True or False. but not the whitespace in between the string.
print(c.endswith("Manoj", 4, 9)) # checks if the substring from index 4 to 11 ends with "Manoj".& it will be same as startwith() method. but not the whitespace in between the string.
print(c.endswith("Manoj", 4, 10)) 
e = 'My name is Manoj Mewara, and my short name is MTR.'
print(e.find('is')) # finds the first occurrence of the substring 'is' and returns its index. 
print(e.find("has")) # returns -1 because the substring "has" is not found in the string.
print(e.index('is')) # finds the first occurrence of the substring 'is' and returns its index. 
# print(e.index("has")) # it is same as find(). but if the substring is not found, it raises a ValueError.
print(e.isalpha()) # only for a-z & A-Z. but, not for the numbers. It isn't contains the whitespace between numbers.
f = 'Manoj555'
print(f.isalnum()) # checks if the string is alphanumeric (contains only letters and numbers). but not the whitespace in between the string.
print(c.islower()) # checks if all characters in the string are lowercase. but not the whitespace in between the string.
print(c.isupper()) # checks if all characters in the string are uppercase. but not the whitespace in between the string.  
print(e.isprintable()) # it is returns true if all the values are printable. like \n is not printable so it wiil give false. but not the whitespace in between the string.