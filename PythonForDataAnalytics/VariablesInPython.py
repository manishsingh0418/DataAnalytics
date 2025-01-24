#Local Variables:

x=24
print("First variable x" , x)
def hello():
    x=25
    return x
print(hello())

print(x)


#Global Variable


x=24
print("First variable x" , x)
def hello():
    global x
    x=25
    return x
print(hello())

print(x)
