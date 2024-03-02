import re       #re - regular expression module, 
                #RegEx can be used to check if a string contains the specified search pattern



print("Create a password with following requiurements: \n At least 8 characters long \n At least one uppercase letter \n At least one lowercase letter \n At least one digit \n At least one special character")
print ("           ")

while True:
password = input ("Create a password: ")
if len (password) < 8:
    print ("The password must be at least 8 characters")
elif not re.search("[a-z]", password):
    print("The password must contain at least 1 lowercase letter")
elif not re.search("[A-Z]", password):
    print("The password must contain at least 1 upppercase letter")    
elif not re.search("[0-9]", password):
    print("The password must contain at least 1 digit")    
elif not re.search("[~!@#$%^&*]", password): 
    print("The password must contain at least 1 special character")
else:
    print ("Password accepted")  
break  
    

