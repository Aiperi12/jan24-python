persons = [{ "name" : " Kumo",
            "age" : "23",
            "salary" : "15000",
            "items" : "car, laptop, tv, monitor",
},
        {   "name" : " Mike",
            "age" : "20",
            "salary" : "10000",
            "items" : "car, PC, smart-watch, boat",

}
]

for person in persons:
    for info in person.items():
        print (info)