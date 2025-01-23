a=("Oneplus","Vivo","Redmi","Samsung","Nokia")
# Slicing Tuples
# print(a[1:3])
# print(a[:3])
# print(a[2:])
# print(a[1::2])
# print(a[::-1])
# print(a[2::-1])
#


#Iterating Tuples

#With for loop
for i in a:
    print(i)
#Along with range and length in for loop
for i in range (len(a)):
    print(a[i])
#along with while loop
i=0
while i<len(a):
    print (a[i])
    i+=1