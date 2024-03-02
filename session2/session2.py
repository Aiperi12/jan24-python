inp = int(input("Give your number: "))
var = 10
if inp > var:
    print("Your number is greater than 10")   #space = tab = indentation
else:
    print("Your number is less than 10")    
print("        \n -------------")



inp = int(input("Give your number: "))
if inp % 2 == 0:          #numbers divided by 2, remainder is equal 0
    print ("The number is even")

elif inp % 2 ==1:          #numbers not divided by 2, remainder is not equal 0
    print("The number is odd") 

else:
    print("You didn't put whole numbers")    
print("        \n -------------")



age = int(input("What is your age?: "))
if age > 0 and age <15:
    print("You are kid")
elif age >= 15 and age <20:
    print("You are teenager")    
elif age >=20 and age <=100:
    print("You are an adult")
else:
    print("Please provide correct age")
print("        \n -------------")



print ("If you are agree, choose one of the answers: Yes, yes, Y ,y")
print ("If you aren't agree, choose one of the answers: No, no , N, n")
inp = input ("What is your answer?: ")
if inp == "n" or inp == "N" or inp == "no" or inp == "No":
    print ("You answered No")
elif inp == "yes" or inp == "Yes" or inp == "y" or inp == "Y":
    print ("You answered Yes")    
print("        \n -------------")



for num in range(10):
    print (num)     
print("        \n -------------")



var = int(input("Please enter the number: "))   
for num in range(var):
    print (num)    
print("        \n -------------")



for letter in "Hello":
    print(letter)    
print("        \n -------------")



word = input("Please enter your word: ")
for letter in word:
    print(letter)
print("        \n -------------")



var1 = input(int("Please enter your number: "))
for num in range (var1):
    print (num)
print("        \n -------------")



var = 0
while var != 10:
    print(var)
    var = var + 1
print ("This is the end ", var)    
print("        \n -------------")


x=0
while x < 10:
    x = x + 1
    print(x)
