#!/usr/bin/python

#class employee name and salary
#have 2 functions:display employee name and salary 

class employee:
    def __init__(self,_name_,_salary):
       self.name=_name_
       self.salary=_salary

    def display(self):
        print("Employee name is " +self.name,"gets " +self.salary)

employee1=employee("Brendah",str(350000))
employee1.display()
employee1=employee("Maina",str(30000))
employee1.display()
employee1=employee("Caisy",str(50000))
employee1.display()
employee1=employee("Bambi",str(550000))
employee1.display()