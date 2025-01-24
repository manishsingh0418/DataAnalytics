#Write a function to find maximum of three numbers in python
def maximum_num(val1,val2,val3):
    if val1>val2 and val1>val3:
        print(val1,"is the greatest number")
    elif val2>val1 and val2>val3:
        print(val2,"is the greatest number")
    else:
        print(val3, "is the greatest number")
maximum_num(12,5,9)
#Write a Python function to create and print a list where the values square of numbers between 1 and 30
def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)

    return l
print(create_list())

#Write a Python function that takes a number as a parameter and check if the number function is prime or not
def check_prime(num):
    if num ==1:
        print("It is not a prime number ")
    if num ==2:
        print("iT IS A PRIME NUMBER")
    if num>2:
        for i in range(2, num):
            if num % i == 0:
                print("It is not a prime number")
                break
        else:
            print("It is a prime number")

check_prime(37)
#Write a Python function to sum all the numbers in a list
def add(numbers):
    total=0
    for i in numbers:
        total =total+i
    return(total)
print(add([12,4,5,6,7,8] ))
#Write a python program to solve the fibonacci sequencw using recurssion
def fs(num):
    if num==1:
        return(0)
    elif num==2:
        return(1)
    else:
        return (fs(num-1)+fs(num-2))

print(fs(7))