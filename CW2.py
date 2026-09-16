mylist = []
while 1:
    print("Mylists")
    print("1. Add element")
    print("2. Remove element")
    print("3. Replace element")
    print("4. Sort elements")
    print("5. Print")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6):"))

    if choice == 6:
        print("Exiting...")
        break

    elif choice == 1:
        element = int(input("Enter an element to add: "))
        mylist.append(element)
        print(f"{element} is added to the list.")

    elif choice == 2:
        element = int(input("Enter an element to remove: "))
        if element in mylist:
            mylist.remove(element)
            print(f"{element} is removed from the list.")
        else:
            print("Element not in the list.")

    elif choice == 3:
        old_element = int(input("Enter element you want to replace: "))
        if old_element in mylist:
            new_element = int(input("Enter new element: "))

            index = mylist.index(old_element)
            mylist[index] = new_element
            print(f"{old_element} is now replaced by {new_element}.")

        else:
            print(f"{old_element} is not in the list.")

    elif choice == 4:
        mylist.sort()
        print("List is sorted.")

    elif choice == 5:
        print("My list is:")

        if len(mylist) == 0:
            print("List is right now empty.")

        else:
            for item in mylist:
                print(item)

    else:
        print("Invalid choice. Enter a number from 1-6.")



