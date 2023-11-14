import json
from getpass import getpass

def load_data():
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_data(data):
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

def get_master_password():
    return getpass("Enter your master password: ")

def show_passwords(data, master_password):
    if master_password == get_master_password():
        for username, password in data.items():
            print(f"Username: {username}, Password: {password}")
    else:
        print("Incorrect master password.")

def add_password(data, master_password):
    if master_password == get_master_password():
        username = input("Enter the username: ")
        password = getpass("Enter the password: ")
        data[username] = password
        save_data(data)
        print("Password added successfully.")
    else:
        print("Incorrect master password.")

def main():
    MASTER_PASSWORD = get_master_password()
    data = load_data()

    while True:
        print("\n1. Show Passwords\n2. Add Password\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            show_passwords(data, MASTER_PASSWORD)
        elif choice == "2":
            add_password(data, MASTER_PASSWORD)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

