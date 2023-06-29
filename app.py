import time

admin_username = "EpiK"
admin_password = "password"

def menu():
    print("Welcome to the EpiK Admin Panel version 0.1")
    print("A. View all users")
    print("B. View banlist")
    print("C. Kick")
    print("D. Ban")
    
    response = input("What would you like to do?: ")
    
    if response == "A" or response == "a":
        users()
    elif response == "B" or response == "b":
        banList()
    elif response == "C" or response == "c":
        kick()
    elif response == "D" or response == "d":
        ban()
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
        print(user)
        
    userList.close()
    
def banList(): ## FIXED WITH GPT :)
    banlist_response = input("Would you like to view the ban list? Y/N:")
    if banlist_response.lower() == "y": ## FIXED INSTEAD OF USING Y OR y
        banListFile = open("banlist.txt", "r")
        for user in banListFile:
            print(user)
        banListFile.close()
    else:  ## INSTEAD OF VIEWING FILE AND CLOSING, MAKE IT ASK IF YOU WANNA VIEW IT AGAIN OR GO BACK TO MENU
        print("Returning to menu")
        time.sleep(3)
        menu()

def kick():
    print("Kick")

def ban():
    banListFile = open("banlist.txt", "a")
    banUser = input("Ban user: ")
    banListFile.write(banUser + "\n")  # Write the banned user to the file
    print(f"You have banned {banUser}!") ## make it return to menu
    
    banListFile.close()
    
# Call the main function to start the program
main()