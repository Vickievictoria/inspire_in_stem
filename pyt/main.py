#!/usr/bin/python

import operations
from students import student
from teachers import Teacher


print(operations.add_numbers(12,4))
print(operations.mult_numbers(12,4))
print(operations.sub_numbers(12,4))
print(operations.div_numbers(12,4))

new_student=student("Liam","exploring",1999)
student.greet_student()

new_Teacher=Teacher("Mr John", 12467,"Literature", 40000)
print(new_Teacher.get_tsc_no())

