# print (oct (43))
# print ((0o54))

# print (hex(30))

# print ("           ")

# names = ["Aiperi", "Abbos", "Dastan", "Khusrav", "Fatima", "Yrys", "Myroslav", "Guliza", "Meerim"]
# for word in names:
#     print ("Hello", word)
# print ("           ")

               #### Tuples

# names = ("Aiperi", "Abbos", "Dastan", "Khusrav", "Fatima", "Yrys", "Myroslav", "Guliza", "Meerim")
# print (type(names))
# print ("           ")

# person = ("John", "Doe", "01-01-1990", "123-12334")
# print (person)
# print ("           ")

# person = ("John", "Doe", "01-01-1990", "123-12334", ["1234-234-234", "234-342-3444"])
# for info in person:
#     print(info)

# person = ("John", "Doe", "01-01-1990", "123-12334", ["1234-234-234", "234-342-3444"])
# person [-1][0] = "8778-786-78678"    ## [] - is list, can change inside of tuples, [-1] - is show list, [0] - access to the first list
# print (person)
# print ("           ")

             ### Dictionaries

# person = { "name" : ("John",),
#         "lastname" : "Doe",
#      "date_of_birth" : "12-12-2012",
#      "SSN" : "234-345"
# }
# for info in person.items():
#     print (info)






# movie1 = { "title" : "Godfather",
#         "year of release" : "1972",
#         "director" : "Francis Ford Coppola",
#         "maim actor" : "Al Pacino"
# }
# movie2 = { "title" : "Forrest Gump",
#         "year of release" : "1994",
#         "director" : "Robert Zemeckis",
#         "maim actor" : "Tom Hanks"
# }
# print (movie1)
# print (movie2)


# movies = [ 
#     { "title" : "Godfather",
#         "year of release" : "1972",
#         "director" : "Francis Ford Coppola",
#         "main actor" : "Al Pacino",
# },
#     { "title" : "Forrest Gump",
#         "year of release" : "1994",
#         "director" : "Robert Zemeckis",
#         "main actor" : ["Tom Hanks", "Tom Crise"]
# }
# ]
# for movie in movies:   #  iterating inside of a list -----> dictionary
#     # print (movie["title"])
#     for info in movie.items():    #also can use movie.values
#         print(info)
# print ("                  ")
# # print (movies)
# # print (movies [0]["director"])


#                        ### SETS 
# st = {1,2,3,3,3,3,2,2,2,1,1,1,"Hello", "Hello"}
# print (st)
# print ("                  ")

# lst = {1,2,3,3,3,3,2,2,2,1,1,1,"Hello", "Hello"}
# st = set (lst)                  #### convert the lst to st
# lst = list (st)
# print (lst[-1])
# print ("                  ")

# set_a = {1,2,3,4,5}
# set_b = {4,5,6,7,8}

# union_set = set_a & set_b      # print only same values
# union_set1 = set_a | set_b     #sort 2 sets together
# print(union_set)
# print (union_set1)

      ###Comprehension

lst = []
for num in range (10):
    lst.append(num)
print (lst)

lst = [num for num in "Hello"]    ### [value] | for loop
print(lst)

fruits = ["apple", "banana", "kiwi", "mango", "cherry"]
lst = [fruit for fruit in fruits if 'a' in fruit]            # print inly fruits with letter a
print (lst)


d = [i : i ** 2 for i in range (4)]
print (d)