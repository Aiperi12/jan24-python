chr = "<< >>"
str = "hello"
new_string = chr [:2] + str + chr [-2:] 
print (new_string)
print ("           ")


str4 = "aabb"
str5 = "hello"
output = str4 [:2] + str5 + str4 [2:]
print (output)