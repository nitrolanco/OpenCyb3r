import sys
import os

# Ensure the "Password Analyzer Builder" folder is accessible
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Password Analyzer Builder'))

def show_menu():
    print("\nWelcome to OpenCyb3r")
    print("=====================")
    print("1. Hash Generator")
    print("2. Password Strength Analyzer")
    print("3. Exit")
    return input("Choose an option: ")

def hash_generator_tool():
    import hash_generator  # Importing inside function to avoid unnecessary memory usage
    hash_generator.main()

def password_analyzer_tool():
    import example_password_analyzer  # Import inside function to prevent unwanted execution
    while True:
        password = input("Enter your password (or type 'back' to return to the menu): ")
        if password.lower() == 'back':
            break
        strength = example_password_analyzer.check_password_strength(password)
        print(f"Password Strength: {strength}/5")
        if strength < 3:
            print("Your password is weak. Consider making it longer and using a mix of upper and lower case letters, numbers, and special characters.")
        elif strength < 5:
            print("Your password is moderate. You could improve it by adding more variety.")
        else:
            print("Your password is strong. Good job!")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            hash_generator_tool()
        elif choice == "2":
            password_analyzer_tool()
        elif choice == "3":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
