Student ={"name":"John","Class":"6th","roll_no":23}

#get
x=Student.get("name")
print(x)

#keys
b=Student.keys()
print(b)

#Values
c=Student.values()
print(c)

#copy
d=Student.copy()
print(d)

#setdefault
x=Student.setdefault("roll_no",24)
print(x)

#update
#pop
#popitem
#clear