import sys
import os
from pathlib import Path

def show_menu():
    print("\nWelcome to OpenCyb3r")
    print("=====================")
    print("1. Example Tool (Coming Soon)")
    print("2. Hash Function (Coming Soon)")
    print("3. TOTP Generator")
    print("4. Exit")
    return input("Choose an option: ")

def example_tool():
    print("\nExample Tool: Replace this with your tool's functionality.")
    input("Press Enter to return to the menu.")

def totp_tool():
    totp_dir = Path("modules/TOTP")
    
    if not totp_dir.exists():
        print("\nError: TOTP module not found!")
        print("Please ensure the TOTP module is installed in the modules directory.")
        input("Press Enter to return to the menu.")
        return

    while True:
        print("\nTOTP Generator")
        print("==============")
        print("1. First Time Setup")
        print("2. Generate New TOTP Key")
        print("3. Get TOTP Code")
        print("4. Return to Main Menu")
        
        choice = input("Choose an option: ")
        
        # Change to the TOTP directory to ensure proper file access
        original_dir = os.getcwd()
        os.chdir(totp_dir)
        
        try:
            if choice == "1":
                if Path("totp_keys.encrypted").exists():
                    print("\nWarning: Setup file already exists!")
                    confirm = input("Do you want to reset and create a new master password? (y/N): ")
                    if confirm.lower() != 'y':
                        print("Setup cancelled.")
                        continue
                
                print("\nInitializing TOTP Setup...")
                os.system(f"{sys.executable} setup.py")
                
            elif choice == "2":
                if not Path("totp_keys.encrypted").exists():
                    print("\nPlease run First Time Setup before generating keys.")
                    continue
                    
                print("\nGenerating new TOTP key...")
                os.system(f"{sys.executable} keygen.py")
                
            elif choice == "3":
                if not Path("totp_keys.encrypted").exists():
                    print("\nPlease run First Time Setup before generating codes.")
                    continue
                    
                print("\nGenerating TOTP code...")
                os.system(f"{sys.executable} otpapp.py")
                
            elif choice == "4":
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        finally:
            # Always return to the original directory
            os.chdir(original_dir)
        
        input("\nPress Enter to continue...")

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            example_tool()
        elif choice == "2":
            print("\nHash Function: Coming Soon!")
            input("Press Enter to return to the menu.")
        elif choice == "3":
            totp_tool()
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()