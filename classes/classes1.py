#!/usr/bin/python



from unicodedata import name


class person:
    def __init__(self,_name_,_age):
        self.name= _name_
        self.age= _age
        
    def sayHi(self):
        print("hello, my name is " +self.name , "I am " +self.age + " years old" )
        
person1=person("bob",str(16))
person1.sayHi()
person2=person("James",str(21))
person2.sayHi()

#create a vehicles class without any variable variables and methods max speed and milage
class vehicle:
    def __init__(vehicle,maxspeed,milage):
         vehicle.maxspeed= maxspeed
         vehicle.milage= milage
    def cars(vehicle):
         print("The max speed is " +vehicle.maxspeed ,"and the mileage is"+vehicle.milage)

vehicle=vehicle("200","300")
print(vehicle.maxspeed,vehicle.milage)
vehicle.cars()

audi = vehicle(500,450)
mercedes =vehicle("300","500")
jaguar=vehicle("350","400")
print(audi.maxspeed,audi.milage)
print(mercedes.maxspeed,mercedes.milage)
print(jaguar.maxspeed,jaguar.milage)


