# a={"Ironman","Hulk","Thor","Captain America"}
#
# #add
# a.add("Spiderman")
# print(a)
#
# #pop
# a.pop()
# print(a)
#
# #remove
# a.remove("Thor")
# print(a)
#
# #discard
# a.discard("Hulk")
# print(a)
#
# #copy
# b=a.copy()
# print(b)

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor"}

# #isdisjoint
# print(a.isdisjoint(c))
#
# #issubset
# print(a.issubset(b))
#
# #issuperset
# print(a.issuperset(c))
#
# #update
# a.update(c)
# print(a)
#
# #clear
# a.clear()
# print(a)

#union

print(a.union(c))

#Difference

print(a.difference(c))

#Difference Update

a.difference_update(c)
print(a)

#Intersection
print(a.intersection(c))

#Intersection Update
a.intersection_update(c)
print(a)

#symmetric difference