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
    print("Users list")

def banList():
    print("Ban list")

def kick():
    print("Kick")

def ban():
    print("Ban")

# Call the main function to start the program
main()
