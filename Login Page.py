# Simple user "database"
users_db = {
    "admin": "password123",
    "python_fan": "code4life"
}

def login_system():
    logged_in = False
    current_user = None

    print("--- Welcome to the Python Secure Portal ---")

    while True:
        if not logged_in:
            print("\n1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")

                # Logic Check: Does the user exist and does the password match?
                if username in users_db and users_db[username] == password:
                    print(f"\n[SUCCESS] Welcome back, {username}!")
                    logged_in = True
                    current_user = username
                else:
                    print("\n[ERROR] Invalid username or password.")

            elif choice == "2":
                new_user = input("Create Username: ")
                if new_user in users_db:
                    print("\n[ERROR] Username already exists!")
                else:
                    new_pass = input("Create Password: ")
                    users_db[new_user] = new_pass
                    print("\n[SUCCESS] Account created! You can now login.")

            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

        else:
            # The "Member Only" Area
            print(f"\n--- DASHBOARD (User: {current_user}) ---")
            print("1. View Secret Message")
            print("2. Logout")
            member_choice = input("Choose an option: ")

            if member_choice == "1":
                print("\n>>> SECRET: Python is awesome! <<<")
            elif member_choice == "2":
                print(f"\nLogging out {current_user}...")
                logged_in = False
                current_user = None

# Run the system
login_system()