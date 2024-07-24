def main():
    #Obtain the password from the user
    password = input("Enter the password :")
    check_password_strength(password)

def check_password_strength(password):
    if len(password) < 8:
        print("The password lenth should be more than 8 !")

main()