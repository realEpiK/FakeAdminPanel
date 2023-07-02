import time
import sys


admin_username = "EpiK"
admin_password = "password"

def menu():
    print("Welcome to the EpiK Admin Panel version 0.1")
    print("A. View all users")
    print("B. View banlist")
    print("C. Kick")
    print("D. Ban")
    print("E. Exit")
    
    response = input("What would you like to do?: ")
    if response.lower() == "a":
        users()
    elif response.lower() == "b":
        banList()
    elif response.lower() == "c":
        kick()
    elif response.lower() == "d":
        ban()
    elif response.lower() == "e":
        exit()
    else:
        print("Invalid option.")

def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    logged_in = False

    if username == admin_username and password == admin_password:
        print(f"Welcome, {username}!")
        logged_in = True
        menu()  # Call the menu function if logged in successfully
    else:
        print("Invalid username or password.")

def users():
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
        return users()
    
def banList():
    banListFile = open("banlist.txt", "r")
    for user in banListFile:
        print(user.strip())
    banListFile.close()

        
    menuReturn = input("Return to menu? Y/N: ") ## yes i know its asking you twice, at least im doing something
    if menuReturn.lower() == "y":
        print("Returning to menu...")
        time.sleep(3)
        menu()
    else:
        return banList()
    
def kick():
    userList = open("userlist.txt", "r")
    userkick = userList.readlines()
    userList.close()  # Close the file after reading
    
    kickuser = input("Kick: ")
    
    if kickuser in userkick:
        print(f"User {kickuser} has been kicked")
    else:
        print(f"{kickuser} was not found in the list.")
    
    menuReturn = input("Return to menu? Y/N: ") ## yes i know its asking you twice, at least im doing something
    if menuReturn.lower() == "y":
        print("Returning to menu...")
        time.sleep(3)
        menu()
    else:
        return kick()

def ban():
    banListFile = open("banlist.txt", "a")
    banUser = input("Ban user: ")
    banListFile.write(banUser + "\n")  # Write the banned user to the file
    print(f"You have banned {banUser}!") ## make it return to menu
    
    banListFile.close()
    
    returnUser = input("Return to menu? Y/N: ")
    if returnUser.lower() == "y":
        print("Returning to menu...")
        time.sleep(3)
        menu()
    else:
        return ban()
    
def exit():
    print("Exiting...")
    time.sleep(3)
    sys.exit()
    
# Call the main function to start the program
main()