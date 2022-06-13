#!/usr/bin/python

#what is a dictionary
#syntax for dictionary
#define,add,delete
#looping of a dictionary
#a list inside a dictionary,dictionaries in list and dictionaries in dictionaries.
# a dictionary is a collection of key value
#syntax; dictionaries={'key':'value'}
colors=['red','green','blue','grey']
i=0
while i <len(colors):
    if (colors[0]=='red'):
        print(colors[0].upper())
        i+=1
for color in colors:
    if(color[0]=='red'):
        print(colors[0].upper())
        i+=1#terminates the loop


vehicles={'type':'toyota','plate_number' :'402'}

    
#accessing values inside the dictionaries
#print(vehicles['type'],vehicles['plate_number'])#you acn access the value of an element

#dictionary person
person={
    'name':'Stewie',
    'gender':'female',
    'address':'Nairobi',
    'phone_number':'0743567889'
    }
person ['age'] ="21"
person ['color']="grey"
del person['gender']
#print(type[person])
print(person)

#looping over dictionaries
for key,value in person.items():
    print(f"{key}:{value}")
    #print every color in uppercase using a loop.









