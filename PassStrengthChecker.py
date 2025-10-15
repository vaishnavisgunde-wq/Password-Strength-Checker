import os 
import time
import pwinput
import re

# Renamed the global list to avoid conflict with the function name
password_storage = []

def validate_and_store_password():
    # Use pwinput to securely prompt for the password (masking the input)
    pw = pwinput.pwinput(prompt="Enter password to validate: ", mask="*")

    # Define the password strength criteria
    is_long_enough = len(pw) >= 8  # Increased min length to 8, a common security standard
    has_digit = re.search(r"[0-9]", pw)
    has_special_char = re.search(r"[!@#$%^&*()_+={}|[\]\\:;\"'<>,.?/`~-]", pw) # Expanded special character set
    has_lowercase = re.search(r"[a-z]", pw)
    has_uppercase = re.search(r"[A-Z]", pw)

    if (is_long_enough and 
        has_digit and
        has_special_char and 
        has_lowercase and
        has_uppercase):

        print("Password strong enough! Storing...")
        time.sleep(1)
        
        # Append to the distinct global list
        password_storage.append(pw)
        print("Stored Passwords:", password_storage)
    else:
        print("\nPassword is too weak!")
        print("--- Requirements ---")
        # Provide specific feedback to the user
        if not is_long_enough:
            print("- Must be at least 8 characters long.")
        if not has_digit:
            print("- Must contain at least one digit (0-9).")
        if not has_special_char:
            print("- Must contain at least one special character (e.g., !@#$).")
        if not has_lowercase:
            print("- Must contain at least one lowercase letter (a-z).")
        if not has_uppercase:
            print("- Must contain at least one uppercase letter (A-Z).")

# Call the correctly named function to run the logic
validate_and_store_password()