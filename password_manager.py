import os.path
import sys

#check for file/create new file
def checkSystem():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

#new password in txt file
def newPass():
    file = open("info.txt", 'a')

    print()
    print()

    username = input("please enter the username here: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website here: ")

    print()
    print()

    usrnm = "Username: " + username + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"



    file.write("~~~~~~~~~~"+(website)+"~~~~~~~~~~\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write("\n")
    file.close()
    print("Password Added!")
    print()
    menu()

def viewPass():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)

def menu():
    print("1. System Check")          #Menu
    print("2. Add New Password")
    print("3. View Passwords")
    print("4. Exit")
    print("5. Help")
    menu_selection = input("Please choose an item from the menu above: ")

    if menu_selection == "1":         #menu selection
        checkSystem()
        menu()
    elif menu_selection == "2":
        newPass()
        menu()
    elif menu_selection == "3":
        viewPass()menu()
    elif menu_selection == "4":
        print("Ending program... Goodbye!")
        sys.exit()
    elif menu_selection == "5":
        help()
        menu()
    else:
        print("You did not enter a valid response!")
        menu()

menu()




