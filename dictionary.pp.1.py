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
        key = input("Enter course key: ")
        name = input("Enter course name: ")
        mycourses[key] = name
        print(f"Course '{key}: {name}' added.")

    elif choice == "2":
        key = input("Enter course key to remove: ")
        if key in mycourses:
            del mycourses[key]
            print(f"Course '{key}' removed")

        else:
            print(f"Course '{key}' not found.")

    elif choice == "3":
        key = input("Enter course key to replace: ")

        if key in mycourses:
            new_name = input("Enter course name: ")
            mycourses[key] = new_name
            print(f"Course '{key}: {new_name}' added.")

        else:
            print(f"Course '{key}' not found.")

    elif choice == "4":
        print("My courses:")
        if len(mycourses) == 0:
            print("No courses found.")

        else:
            for course in mycourses:
                print(f"{course}: {mycourses[course]}")
    else:
        print("Invalid choice.")
