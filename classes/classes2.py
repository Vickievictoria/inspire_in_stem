#!/usr/bin/python

def print_name(name ="Vila"):
    print(name)

print_name("Vila")


def get_sum(num1,num2):
    sum_nums = num1+num2
    return sum_nums

print(get_sum(5,4))

def get_powers(number,power):
    power_nums=number**power
    return get_powers

print(get_powers(6,3))



def print_fullname(f_name,s_name):
    fullname=f_name + s_name
    return print_fullname.title

print(print_fullname("Madonna","Sudy"))

#returning a dictionary
def create_fullname(first_name,second_name):
    person={'first':'Jason',
            'second': 'Kerian'
    }
    return person

    ##### list in a function

def greatfriends(names):
    for name in names
    msg="Hello" +name.title()+"!"
    print(msg)

friends=["syd","rodney","vis","ella"]