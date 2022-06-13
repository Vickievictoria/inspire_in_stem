#!/usr/python
mary_fav_pizza=['beef','chicken','pineapple']
jane_fav_food=['rice','ugali','choma']
edibles={
    'mary':['beef','chicken','pineapple'],
    'jane':['rice','ugali','choma']
    }
print(edibles)
#print mary and jane:name,email and password
mary={'name':'Mary','email':'mary@gmail.com','password':'MARY1'}
jane={'name':'Jane','email':'jane@gmail.com','password':'JANE1'}
person={
    'name':['Mary','Jane'],
    'email':['mary@gmail.com','jane@gmail.com'],
    'password':['MARY1','JANE1']
}
print(mary)
print(jane)
print(person)
for key,value in person.items():
    print(f"{key}:{value}")
