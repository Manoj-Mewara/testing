A = 5 * 2j
print(A)
print(type(A))
B = complex(5, 6)
print(B)
print(type(B))
a = 9
b = 2.4
c = 2/4J
d = False
e = "Hello"
f = None
print("The type of a is:", type(a))
print("The type of b is:", type(b)) 
print("The type of c is:", type(c))
print("The type of d is:", type(d))         
print("The type of e is:", type(e))
print("The type of f is:", type(f))

g = {1, 2, 3, 4, True, 5}
print("The type of g is:", type(g))
print(g)

list1 = [3, 9.0, "MTR", ["Lion", "Cat"]]
print(list1)
tuple1 = (3, 9.2, "MTR", ("Lion", "Cat"))
print(tuple1)
dict1 = {"Name": "Manoj", "Nickname": "MTR", "Age": 18, "Gender": "Male", "CanVote": True}
print(dict1)

tuple1 = (10, 20, 30)
tuple1[0] = 99  # Iska matlab hai: Tuple ke pehle number (10) ko hatakar 99 kar do