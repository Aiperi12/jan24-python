
for i in range (1, 4):
    for j in range (1, 5):
    for k in range (1, 5):
            
print ("           ")

names = ["Aiperi", "Abbos", "Dastan", "Khusrav", "Fatima", "Yrys", "Myroslav", "Guliza", "Meerim"]
print (names[1][0])
print (names[1][0:2])
print (names[2 : 3])
print (names[::-1])

print ("           ")

for name in names:
    print(name[::-1])

print ("           ")
 
numbers = [10, 10.4, 90, 110, 10, 23.3]
sum = sum (numbers)
print (sum)

print ("           ")

names = ['Aiperi', "Abbos", "Dastan", "Khusrav", "Fatima", "Yrys", "Myroslav", "Guliza"]
names.append ("Esen")             #add the element
names.insert(2,"Esen")            #add the element in the specific place
del names [-1]                    #delete the element by the index of elements
names.remove("Abbos")             #delete the element by the name of elements
names.pop ()                      #delete the last element of the list     
names.sort ()                     #sort in alphabetic order
names.sort(reverse=True)          #sort in back alphabetic order
print (names)

print ("           ")