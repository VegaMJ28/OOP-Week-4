mycourses = {"",""}

while 1:
    print("1. Add course")
    print("2. Remove course")
    print("3. Replace course")
    print("4. Print course")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == 5:
        print("Exiting...")
        break

    elif choice == 1:
        course_name = input("Enter your course: ")
        mycourses.update({"c_name1": course_name})

    elif choice == 2:
        course_name = input("Enter your course: ")

        if course_name in mycourses:
            del mycourses ["course_name"]

        else:
            print("Course does not exist")

    elif choice == 3:
        
