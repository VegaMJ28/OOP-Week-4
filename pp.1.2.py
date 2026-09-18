mycourses = {}

while 1:
    print("Course dictionary")
    print("1. Add course")
    print("2. Remove course")
    print("3. Replace course")
    print("4. Print course")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting...")
        break

    elif choice == "1":
        number_of_courses = int(input("Enter number of courses you want to add: "))
        for course in range (0,number_of_courses ):
            course_name = input("Enter course name: ")
            mycourses.update({"course"+str(i):course_name})

       # i = i+1

