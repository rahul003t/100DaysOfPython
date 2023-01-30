
"""
In this exercise I import time module and based on time it give the suitable output 
"""


import time
str=input('Enter your name : ')
hours = int(time.strftime('%H'))
if(hours>=0 and hours<=11):
  print("Hello ",str.capitalize(),", Good Morning ")
elif(hours>=12 and hours<=17):
  print("Hello ",str.capitalize(),", Good Afternoon ")
else:
  print("Hello ",str.capitalize(),", Good Evening ")
