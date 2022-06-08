#!/usr/bin/python
import random
print("welcome to our password generator")

#ask user number of paswords they want to generate
#ask usr for password length
#num_passwords convert to iteger
#len_password convert to integer
character='banana101'
num_password=int(input("How many password do you want to generate"))
len_password=int(input("What length do you want your password to be"))
print("Here are your passwords")

for password in range(num_password ):

    password=''
    for c in range(len_password):
        password += random.choice(character)

    print(password)
