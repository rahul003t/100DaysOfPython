# here I am dicussing different types of String methonds in Python
# .upper() method used to convert the string into upper case eg: abc --> ABC
# .lower() method is used to convert the string into lower case eg: ABC ---> abc
# some other metghod are given below

################################################################

a = "Rahul Gorai"
print(len(a))
print(a)
print(a.uppercase())
print(a.lowercase())

 
"""
Output:
11
Rahul Gorai
RAHUL GORAI
rahul gorai
"""

str = "Rahul!!!"
print(str.rstrip("!"))
print(str.endwith("!!!")
      
"""
Output:
Rahul
True
"""
# find method is find the string , if no find then it return -1
str1 = "Rahul is a Good Developer"
print(str1.find("Developer")
print(str1.find("Student")
      
 """
 Output:
 True
 -1(error)
 """
 # .isalnum() method is used if the string contain A-Z, a-z,0-9 , if not contains return false
 str2 = "HelloWorld"
 print(str1.islnum())
 """
 Output:
 True
 """
 # .isspace() method is used return true if the string having space ot tap
 str3 = "Rahul is     good Developer"
 print(str3.isspace())
  """
  Outrput:
  True
  """
  # .startwith() method is return true if the given argument is start with the same of string starting word
  
  srt4="Rahul is Good"
  print(str4.startwith("Rahul"))
  print(str4.startwith("Rohan"))
      
  """
  Output:
  True
  False
  """
      
      
      
       
      
  
  
  
