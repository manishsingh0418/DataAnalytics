# def add ():
#     x=56
#     y=23
#     print(x+y)
# add()

#Parameter and Arguments

# def rect (length,width):
#     print("the area of the rectangle is ",length*width)
#
# rect(12,7 )

#Arbitary Argument

def hello(*name):
    print("hello my name is", name[2])
hello("John","Lisa","Peter")