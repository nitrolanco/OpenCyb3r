#!/usr/bin/python3

def check_password_strength(password):
    
    import re
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


def run_main():
    password = input("Enter your password:")
    
    strength = check_password_strength(password)
    print(f"\nPassword Strength: {strength}/5\n")
    if strength < 3:
        print("Your password is weak. Consider making it longer and using a mix of upper and lower case letters, numbers, and special characters.\n")
    elif strength < 5:
        print("Your password is moderate. You could improve it by adding more variety.\n")
    else:
        print("Your password is strong. Good job!\n")
    

if __name__ == "__main__":
    print("\nWelcome to the OpenCyb3r Password Analyzer!\n")
    run_main()
