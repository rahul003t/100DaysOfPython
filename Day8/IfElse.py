# Here I am discussing about IF Else codition 
# Conditional Operator in Python
# ----->      <  , > , >=, <= , == , !=       <---

a = 18
print(a>18)
print(a <18)
print(a==18)
print(a <=18)
print(a >=18)
print(a!=18)

"""
Output:
False
False
True
True
True
False

"""

### if-else statement ###

num =10
if(num==0):
  print("This is Zero")
else:
  print("This is Greater than Zero")

 """
 Output:
 This is Greater than Zero
 
 """
### elif statement ###

age =18

if(age < 18 ):
  print("You cannot vote")
eleif( age ==18 ):
  print("Your are Eligible for Vote")
else:
  print("Invalid input")
  
  
"""
Output:
Your are Eligible for Vote

"""

### Nested IF-ELSE ###

num=10

if(num>0):
  if(num>=1 and num<=5):
    print("The number is in between 5")
  else:
    print("The number is greater than 5")
else:
  print("Invalid number")
  
  
"""
Output:
The number is greater than 5

"""
 




















  
