mylist = [1,2,3,4,5,6,7]
print(mylist)

mylist.append(int(input("Add a number to the list: ")))

#mylist.append(int(input("Add another number: ")))
#print(mylist)

old_element = int(input("Enter number you want to replace: "))
if old_element in mylist:
    new_element = int(input("Enter the number to replace for: "))
    index = 0
    for i in mylist:
        if i == old_element:
            break
        index = index + 1
    mylist[index] = new_element
    print("Your list is now:",mylist)


mylist.remove(int(input("Remove a number: ")))
print(mylist)



for i in mylist:
    print(i)

mylist.sort()
print(mylist)

#index= mylist.index(old_element)
#mylist[index] = new_element

