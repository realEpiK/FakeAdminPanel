import time
import sys


admin_username = "EpiK"
admin_password = "password"

def menu(): # Main menu
    print("Welcome to the EpiK Admin Panel version 0.1")
    print("A. View all users")
    print("B. View banlist")
    print("C. Kick")
    print("D. Ban")
    print("E. Exit")
    
    response = input("What would you like to do?: ")
    if response.lower() == "a":
        view_all_users()
    elif response.lower() == "b":
        view_ban_list()
    elif response.lower() == "c":
        kick_user()
    elif response.lower() == "d":
        ban_user()
    elif response.lower() == "e":
        exit_program()
    else:
        print("Invalid option.")
        

def main(): # Login panel 
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    logged_in = False

    if username == admin_username and password == admin_password:
        print(f"Welcome, {username}!")
        logged_in = True
        menu()  
    else:
        print("Invalid username or password.")

def view_all_users(): # Displays user list
    userList = open("userlist.txt","r")
    for user in userList:
        print(user.strip())
    userList.close()
    
    menuReturn = input("Return to menu? Y/N: ")
    if menuReturn.lower() == "y":
        print("Returning to menu...")
        time.sleep(3)
        menu()
    else:
        return view_all_users()
    
def view_ban_list(): # Displays ban list
    banListFile = open("banlist.txt", "r")
    for user in banListFile:
        print(user.strip())
    banListFile.close()

        
    menuReturn = input("Return to menu? Y/N: ") 
    if menuReturn.lower() == "y":
        print("Returning to menu...")
        time.sleep(3)
        menu()
    else:
        return view_ban_list()
    
def kick_user(): # Able to "kick" user
    userList = open("userlist.txt", "r")
    userkick = userList.readlines()
    userList.close()
    
    kickuser = input("Kick: ")
    
    if kickuser in userkick:
        print(f"User {kickuser} has been kicked")
    else:
        print(f"{kickuser} was not found in the list.")
    
    menuReturn = input("Return to menu? Y/N: ") 
    if menuReturn.lower() == "y":
        print("Returning to menu...")
        time.sleep(3)
        menu()
    else:
        return kick_user()

def ban_user(): # Able to "ban" user
    banListFile = open("banlist.txt", "a")
    banUser = input("Ban user: ")
    banListFile.write(banUser + "\n")  
    print(f"You have banned {banUser}!") 
    
    banListFile.close()
    
    returnUser = input("Return to menu? Y/N: ")
    if returnUser.lower() == "y":
        print("Returning to menu...")
        time.sleep(3)
        menu()
    else:
        return ban_user()
    
def exit_program(): # Exiting program
    print("Exiting...")
    time.sleep(3)
    sys.exit()
    
def return_to_menu(): # Returns to menu, it works, but if the user says no, it wont work.
    menu_return = input("Would you like to return to menu? Y/N: ")
    if menu_return.lower() == "Y":
        print("Returning to menu...")
        time.sleep(3)
        menu()
    else:
        return_to_menu()
        
    
# Call the main function to start the program
main()