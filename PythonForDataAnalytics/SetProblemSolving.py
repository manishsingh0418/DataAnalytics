#Write a program to find max and min in a set
# a={12,56,34,8,90,1,57}
# maximum=max(a)
# minimum =min(a)
# print("The maximum value in the set is ",maximum)
# print("The minimum value in the set is ",minimum )

#Write a program to find common elements in three lists using sets
#
# a=[1,5,6,8,2]
# b=[4,5,6,7]
# c=[1,9,6,2,5]
#
# print(set(a) & set(b) & set(c))

#Write a program to find difference between two sets

# a={1,5,6,8,2}
# b={4,5,6,7}
#
# print(a.difference(b))

#Write a program to remove an item from aset if it is present in the set

a={1,5,6,8,2}
a.discard(8)
print(a)

#Write a python program to check if a set is a subset of another set

a={1,2,3,4,5,6}
b={2,3,4}

print(a.issubset(b))

