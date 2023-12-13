import hashlib
import getpass

# Dictionary to store hashed passwords with usernames
password_manager = {}

def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")

    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Store the username and hashed password in the dictionary
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Hash the entered password and compare with stored hashed password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Successful!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
