#!/usr/bin/python

####################
# name: Victoria
#file: operations.py
#date: 6/6/2022
######################
 
import requests
from bs4 import BeautifulSoup as bs

user_name="Victoria"#Iinput("Enter the user name")
url="https://github.com/"+user_name#input("enter site url")
results=requests.get(url)

soup=bs(results.content,"html.parser")
profile_pic=soup.find('img',{'alt':'Avatar'})['src']
print(profile_pic)