#Create a script for a contact list that stores names and phone numbers. The script should include a menu with the following options:
#Add/Modify: Prompts for a name. If the name is in the contact list, it should display the phone number and optionally allow modification if it's incorrect. If the name is not found, it should allow entering the corresponding phone number.
#Search: Prompts for a character string and displays all contacts whose names begin with that string.
#Delete: Prompts for a name and, if it exists, asks if you want to delete it from the contact list.
#List: Displays all contacts in the contact list.
#Implement the script using a dictionary.

agenda = {}
continue_running = True

while continue_running:
    print("\n")
    print("1. Add/Modify")
    print("2. Search")
    print("3. Delete")
    print("4. List")
    print("5. Exit")

    option = int(input("Enter the option you want to perform:"))

    if option == 1:
        name = input("Enter the contact's name:")
        if name in agenda:
            print("%s already exists, their phone number is %s" % (name, agenda[name]))
            option = input("Press 's' if you want to modify it!!!. Any other key to continue.")
            if option == "s":
                number = input("Enter the new phone number:")
                agenda[name] = number
        else:
            number = input("Enter the phone number:")
            agenda[name] = number
    elif option == 2:
        substring = input("Enter the substring to search for contacts:")
        for name, number in agenda.items():
            if name.startswith(substring):
                print("%s's phone number is %s" % (name, agenda[name]))
    elif option == 3:
        name = input("Enter the contact's name to delete:")
        if name in agenda:
            option = input("Press 's' if you want to delete it!!!. Any other key to continue.")
            if option == "s":
                del agenda[name]
        else:
            print("The contact does not exist")
    elif option == 4:
        for name, number in agenda.items():
            print(name, "->", number)
    elif option == 5:
        continue_running = False
    else:
        print("Incorrect option")
