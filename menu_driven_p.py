students = {}

i = 1
while 1:
    print("student dictionary")
    print("1. Add student ")
    print("2. Remove student ")
    print("3. Replace student ")
    print("4. Print ")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting...")
        break

    if choice == "1":
        name = input("Enter student name: ")
        major = input("Enter student major: ")
        year = input("Enter student year: ")

        students.update({"s"+str(i):{"st_name":name,"st_major":major,"st_year":year}})

        i = i + 1

    if choice == "2":
        delete = input("Enter key you want to delete: ")
        del students["delete"]
        print(students)

