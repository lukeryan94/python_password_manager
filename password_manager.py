import os.path
import sys


#check for file/create new file#

def check_system():
    if os.path.exists("info.txt"):
        print("Passwords available!")


    else:
        file = open("info.txt", 'w')
        file.close()
        print("file created!")


# new password in txt file #


def new_pass():

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



    file.write("~~~~~~~~~~~"+(website)+"~~~~~~~~~~~\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write("\n")
    file.close()
    print("Password Added!")
    print()


# view passwords
def view_pass():
        file = open('info.txt', 'r')
        content = file.read()
        file.close()
        print(content)



PASSCODE = "1234"     # passcode to access

connect = input("Please enter passcode: \n")

while connect != PASSCODE:
    connect = input("Please enter correct passcode: \n")
if connect == PASSCODE:       # correct passcode opens menu
    import time
    print("Starting up...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")



    print("Welcome to your password manager v4.3!")
    while True:
        print("1. System Check")  # Menu
        print("2. Add New Password")
        print("3. View Passwords")
        print("4. Exit")
        print("5. Help")
        menu_selection = input("Please choose an item from the menu above: ")

        if menu_selection == "1":  # menu selection
            check_system()

        elif menu_selection == "2":
            new_pass()

        elif menu_selection == "3":
            view_pass()


        elif menu_selection == "4":
            print("Ending program... Goodbye!")
            sys.exit()
        elif menu_selection == "5":
            help()

        else:
            print("You did not enter a valid response!")











