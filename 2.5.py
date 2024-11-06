def main():
    # password validation function
    def is_valid_password(password):
        # password length (between 8 and 20 characters)
        if len(password) < 8 or len(password) > 20:
            return False
        
        # if the password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False
        
        # if the password contains at least one lowercase letter
        if not any(char.islower() for char in password):
            return False
        
        # if the password contains at least one digit
        if not any(char.isdigit() for char in password):
            return False
        
        # if the password contains at least one symbol from the set: !@#$%&*
        valid_symbols = "!@#$%&*"
        if not any(char in valid_symbols for char in password):
            return False
        
        # if all checks pass, return True
        return True
    
    while True:
        # prompt user to enter a password
        password = input("Enter a password: ")

        # checks if the entered password is valid
        if is_valid_password(password):
            print("Password is valid.")
            
            # prompts the user to enter the password again for confirmation
            confirm_password = input("Please confirm your password: ")

            # checks if the passwords match
            try:
                if password == confirm_password:
                    print("Password successfully set!")
                    break  # exits the loop if the passwords match
                else:
                    print("Passwords do not match. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                break  # breaks out of the loop if there's an error

        else:
            print("Password does not meet the criteria. Please try again.")
            
# calls the main function
main()
