#!/usr/bin/python
#print the first terms
#first term=a
#common difference=d
#number of terms=n
a= int(input ("Enter the first number"))
d= int(input("Enter the common difference"))
n= int(input("Enter the number of terms"))
for i in range(1,n+1):
    n_term=a+(i-1)*d
    print(n_term)
    
sum_n=(n_term/2)*(2*a+(n-1)*d)
print(sum_n)

#geometric progression assignment:
