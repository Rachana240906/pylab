class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        else:
            return None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password has been successfully updated.")
        else:
            print("Please choose a different password.")

    def is_correct(self, password_to_check):
        return password_to_check == self.get_password()


manager = Password_manager()

while True:
    print("\nPassword Manager Menu:")
    print("1. Set Password")
    print("2. Get Current Password")
    print("3. Check if Password is Correct")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        new_password = input("Enter new password: ")
        manager.set_password(new_password)
    elif choice == '2':
        print("Current password:", manager.get_password())
    elif choice == '3':
        password_to_check = input("Enter the password to check: ")
        if manager.is_correct(password_to_check):
            print("Password is correct.")
        else:
            print("Password is incorrect.")
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")
