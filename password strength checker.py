import re


def strength_password():
    password = input("enter the password")

    length = len(password)



    has_upper = re.search (r"[A-Z]",password)
    has_lower = re.search (r"[a-z]",password)
    has_digit = re.search (r"[0-9]",password)
    has_special = re.search (r"[!@#$%^&*()_+/|}{}><]",password)


    # checking the condition if the password is strong

    if length < 6:
        strength = "weak"
    elif length <= 12 and (has_upper or has_lower) and has_digit:
        strength = "moderate"
    elif length > 12 and has_upper and has_lower and has_digit and has_special:
        strength = "strong"
    else:
        strength = "weak"

    print(f"your password strength is: {strength}")
strength_password()


import re

def password_strength_checker():
    password = input("Enter your password: ")

    # Check password length
    length = len(password)

    # Define regular expressions for character types
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"[0-9]", password)
    has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Evaluate password strength
    if length < 6:
        strength = "Weak"
    elif length <= 12 and (has_upper or has_lower) and has_digit:
        strength = "Moderate"
    elif length > 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    else:
        strength = "Weak"

    # Output the result
    print(f"Your password strength is: {strength}")

# Call the function to run the program
password_strength_checker()
