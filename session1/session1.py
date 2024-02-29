int1 = 30
int2 = 40

print ("         ")
print (int1 + int2)
print (int1 - int2)
print (int1 * int2)
print (int1 / int2)
print (int1 // int2)
print (int1 % int2)
print (2 ** 3)

print ("----------")

flt1 = 30.3
flt2 = 40.4

print ("         ")
print (flt1 + flt2)
print (flt1 - flt2)
print (flt1 * flt2)
print (flt1 / flt2)
print (flt1 // flt2)
print (flt1 % flt2)

print ("----------")

str1 = """line 1
line 2
line 3 \n"""               # n - add new line

str2 = " World"
str3 = (str1 + str2)
print (str3)

print ("----------")

str4 = "line1 line2\nline3"
print(str4)

print ("----------")

str5 = "Hello World, This is some text and a lot of characters"
print (str5[0:5])      #print words from 0 to 5

print ("----------")

str6 = "Strings in Python are surrounded by either single quotation marks or double quotation marks"
print (str6[0:7])
print (str6 [11:18])
print (str6 [-5:])        #print everything after -5 
print (str6 [:-5])        #print everything before -5

 print ("----------")

inp1 = input("What is your number: ")
inp2 = input("What is your number: ")    #input string through command input 
print(type(inp1 + inp2))

print ("----------")

inp1 = int(input("what is your number?: "))
print (inp1)
print (type(inp1))                      #input integer through command input

print ("----------")

print ("Hello")
print (len("Hello World"))            #count the lenght of the string