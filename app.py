import time
import sys
import os

# Lets add some code to check if banlist.txt and userlist.txt exist, if not, make them!
# Also add code to add users to userlist.txt
# Switch Txt to json -- Forget it, ill learn this later

# in future -  error handling and input validation
admin_username = "EpiK"
admin_password = "password"

def check_files():
    files = ["banlist.txt",'userlist.txt']
    
    for file in files:
        if not os.path.exists(file):
            with open(file,"w"):
                pass
            print(f"{file} has been created!")

def menu(): # Main menu
    
    check_files()
    
    print("Welcome to the EpiK Admin Panel version 0.1")
    print("A. View all users")
    print("B. View banlist")
    print("C. Create user")
    print("D. Kick")
    print("E. Ban")
    print("F. Exit")
    
    response = input("What would you like to do?: ")
    
    choice = response.lower() ## Thanks redox :)
    if choice == "a":
        view_all_users()
    elif choice == "b":
        view_ban_list()
    elif choice == "c":
        create_user()
    elif choice == "d":
        kick_user()
    elif choice == "e":
        ban_user()
    elif choice == "f":
        exit_program()
    else:
        print("Invalid option.")
        

def main(): # Login panel 
    username = input("Enter Username: ")
    password = input("Enter Password: ")
   ##  logged_in = False ## I have no idea what im using this for.

    if username == admin_username and password == admin_password: ## asks for a user and password, if all correct, welcomes user and changes login bool to true, else it prints error
        print(f"Welcome, {username}!")
        ## logged_in = True
        menu()  
    else:
        print("Invalid username or password.")

def view_all_users(): # Displays user list
    userList = open("userlist.txt","r")
    for user in userList:
        print(user.strip())
    userList.close()
    
    menu_return = input("Would you like to return to menu? Y/N: ") ## Asks user if they want to return to menu, if yes, runs function return_to menu, else, it remains on the same function
    if menu_return.lower() == "y":
        return_to_menu()
    else:
        view_all_users()
    
def view_ban_list(): # Displays ban list
    banListFile = open("banlist.txt", "r")
    for user in banListFile:
        print(user.strip())
    banListFile.close()

        
    menu_return = input("Would you like to return to menu? Y/N: ") ## Asks user if they want to return to menu, if yes, runs function return_to menu, else, it remains on the same function
    if menu_return.lower() == "y":
        return_to_menu()
    else:
        view_ban_list()
        
def create_user():
    user_list = open("userlist.txt","a")
    new_user = input("Create user: ")
    
    user_list.write(new_user + "\n")
    print(f"You have created {new_user}!")
    
    user_list.close()
    
    menu_return = input("Would you like to return to menu? Y/N: ") ## Asks user if they want to return to menu, if yes, runs function return_to menu, else, it remains on the same function
    if menu_return.lower() == "y":
        return_to_menu()
    else:
        create_user()

def kick_user(): # Able to "kick" user
    userList = open("userlist.txt", "r")
    userkick = userList.readlines()
    userList.close()
    
    kickuser = input("Kick: ")
    
    if kickuser in userkick:
        print(f"User {kickuser} has been kicked")
    else:
        print(f"{kickuser} was not found in the list.")
    
    menu_return = input("Would you like to return to menu? Y/N: ") ## Asks user if they want to return to menu, if yes, runs function return_to menu, else, it remains on the same function
    if menu_return.lower() == "y":
        return_to_menu()
    else:
        kick_user()

def ban_user(): # Able to "ban" user
    file = open("userlist.txt", "r")
    user = file.read()
    file.close()

    user_ban_input = input("Ban user: ")

    if user_ban_input in user:
        file = open("userlist.txt", "w")
        file.write(user.replace(user_ban_input, "")) ## So i wanted this, but asked chatgpt, so i gotta study how this works more.
        print(f"{user_ban_input} has been banned!")
        file.close()
    else:
        print(f"{user_ban_input} does not exist.")

    
    menu_return = input("Would you like to return to menu? Y/N: ") ## Asks user if they want to return to menu, if yes, runs function return_to menu, else, it remains on the same function
    if menu_return.lower() == "y":
        return_to_menu()
    else:
        ban_user()
    
def exit_program(): # Exiting program
    print("Exiting...")
    time.sleep(3)
    sys.exit()
    
def return_to_menu(): # Returns to menu, it works, but if the user says no, it wont work.
        print("Returning to menu...")
        time.sleep(3)
        menu()
        
# Call the main function to start the program
main()