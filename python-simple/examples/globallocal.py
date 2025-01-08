a = 10 #These are global variables which can be accessed by all the functions defined by the user.
b = 5 
def addition():
  c = 3 #This is a local variable and can only be used within the function addition()
  print(a+b+c)

def substraction():
  print(a-b)

addition() #Function has been called
substraction()
