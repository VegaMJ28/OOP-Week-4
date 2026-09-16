#input("Enter your choice: ")
#if choice == "1" ("" for string"

# Dictionary = {Key : value}  //record
#{"name1":"MJ",}

mydictionary = {"name1": "MJ", "name2": "Jamin", "name3": "Pedro"}
#print(mydictionary["name1"])
print(mydictionary)


mydictionary.update ({"name4":"Elisa"})  # //adding
print(mydictionary)

del mydictionary["name2"] #give elements key //delete
print(mydictionary)

mydictionary["name4"] = "Fiorella" # //replace
print(mydictionary)


fullname = input("Enter your full name: ")
mydictionary.update({"name5":fullname})
print(mydictionary)