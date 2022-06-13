#!/usr/bin/python

#a block of code which gets executed together
#initializing functions and calling the function

def say_hello():
    print("Hello from Vickie")
    x=4
    y=7
    z=y+x
    print(z)

say_hello()

def bark():
    print("dogs bark woof")
def meow():
    print("cats meow")
def neigh():
    print("horses neigh")
bark()
meow()
neigh() 

def add_numbers(x,y):
    sum_numbers = x+y 
    print("the sum of 2 numbers:",sum_numbers)

add_numbers(50,49)
add_numbers(5,9)
add_numbers(32,12)
add_numbers(23,31)

def multiply_numbers(x,y):
    prod_nums=x*y
    print("The product of 2 numbers is",prod_nums)
multiply_numbers(3,5)
multiply_numbers(4,9)

