#!/usr/bin/python3
import re

def check_password_strength(password):
    strength = 0
    # Length check
    if len(password) >= 12:
        strength += 1
    
    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    
    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    
    # Numbers check
    if re.search(r'[0-9]', password):
        strength += 1
    
    # Special character check
    if re.search(r'[!@#$%^&*()]', password):
        strength += 1
    
    # Return strength out of 5
    return strength

def check_rockyou(password):
    with open('rockyou.txt', 'r', encoding='latin-1') as f:
        for line in f:
            if password == line.strip():  # Strip newline characters
                return True  # Found the password
    return False  # Not found

def run_main():
    while True:
        password = input("Enter your password:")
    
        strength = check_password_strength(password)
        print(f"\nPassword Strength: {strength}/5\n")
        if check_rockyou(password):
            print("WARNING!!! Password found in compromised database. Use a more unique password.\n")
        elif strength < 3:
            print("Your password is weak. Consider making it longer and using a mix of upper and lower case letters, numbers, and special characters.\n")
        elif strength < 5:
            print("Your password is moderate. You could improve it by adding more variety.\n")
        else:
            print("Your password is strong. Good job!\n")
    
        print("Enter another password below or press Ctrl+C to exit.\n")

if __name__ == "__main__":
    print("\nWelcome to the OpenCyb3r Password Analyzer!\n")
    run_main()
