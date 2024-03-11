
inp1 = (int(input (" Enter the first number: " )))
inp2 = (int(input (" Enter the second number: " )))
inp3 = (input ("Enter the operation ( +, -, *, /): "))
print (inp1)
print (inp2)
print ("You choose", inp3, "operation")

for inp in inp3:
    if inp3 == "+":
        inp = inp1 + inp2

    elif inp3 == "-":
        inp = inp1 - inp2

    elif inp3 == "*":
        inp = inp1 * inp2  

    elif inp3 == "/":
        inp = inp1 / inp2    

print ("Result", inp)   


