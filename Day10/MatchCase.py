int x =10

match x:
  case 0:
    print("x is Zero")
  case 2:
    print("x is two")
  case 3:
    print("x is three")
  case 4:
    print("x is four")
  #default case  
  case_:
    print("Invalid input")
    
    
"""
Output:
Invalid input
"""

########################################

int x =100

match x:
  case 0:
    print("x is Zero")
  case 2:
    print("x is two")
  case 3:
    print("x is three")
  case 4:
    print("x is four")
  #default case  
  case_ if(x >=100):
    print("X is either 100 or qual to 100")
    
  case_:
    print("Invalid input")
    
    
    
"""
Output:
X is either 100 or qual to 100

"""
  
