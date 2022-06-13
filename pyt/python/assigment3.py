#!/usr/bin/python



gender=input("what gender are you" )
age=int(input("What is your age"))
acc_bal=0

if (age>25) and (age<30):
    acc_bal=acc_bal+10000
    print("your account has been credited with 10000")
else:
    print("you have not been credited")


