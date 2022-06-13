#!/usr/bin/python
from math import factorial

number =input ("number")
factorial=1
if int(number) < 0:
    print("factorial of negative numbers does not exist") 
elif int (number) == 0:
    print("factorial of 0=1")
for i in range (1, int(number)+1):
    factorial=factorial*i
print("factorial of number is: factorial")
print(factorial)
