import re

def main():

        print()

        #Obtain the password from the user
        password = input("Enter the password : ")

        print()

        if ' ' in password:
            print("Password must not contain spaces.")
        else:
            check_password_strength(password)
           

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]',password) is not None
    lower_case_criteria = re.search(r'[a-z]',password) is not None
    number_criteria = re.search(r'[0-9]',password) is not None
    special_character_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]',password) is not None
    
    strength_of_password = 0
    if length_criteria:
        strength_of_password += 1
    if upper_case_criteria:
        strength_of_password += 1
    if lower_case_criteria:
        strength_of_password += 1
    if number_criteria:
        strength_of_password += 1
    if special_character_criteria:
        strength_of_password += 1
    
    strength_level = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print(f"Password strength: {strength_level[strength_of_password-1]}\n")

    if strength_of_password < 5:
        print("Password must:")
        if not length_criteria:
            print(" - be more than 8 characters")
        if not (upper_case_criteria and lower_case_criteria and number_criteria and special_character_criteria):
            print(" - include the following:")
            if not upper_case_criteria:
                print("     - An uppercase letter")
            if not lower_case_criteria:
                print("     - A lowercase letter")
            if not number_criteria:
                print("     - A number")
            if not special_character_criteria:
                print('     - A special character (e.g., !@#$%^&*(),.?\":{}|<>)')
        

main()