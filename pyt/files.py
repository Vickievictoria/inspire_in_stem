#!/usr/bin/python
####################
# name: Victoria
#file: operations.py
#date: 6/6/2022
######################

 #opening a file
f=open("lesson1.txt","x")
print(f.readline())

with open("lesson1.txt","w",encoding='utf8')as f:
    f.write("this is another file \n")
    f.write("coding is interesting \n")
    f.write("learning some more codes \n")

#reading a file
print(f.read())
f.close()
print(f.write())
f.close()


