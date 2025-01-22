a=["Thor","Hulk","Ironman","Captain America"]

#to create a copy of a list
b=[]
print(b)
b=a.copy()
print(b)

# to access an element
print(a.index("Ironman"))

#to extend the list
c=["Vision","Spiderman"]
a.extend(c)
print(a)

# to reverse the list
a.reverse()
print(a)

#to sort the list
a.sort()
print(a)

#to clear all the data from the list
a.clear()
print(a)