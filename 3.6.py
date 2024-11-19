# custom exception class definition
class NotNumericError(Exception):
    """Exception raised for invalid (non-numeric) user input."""
    pass

def main():
    while True:
        try:
            # prompt for user input
            user_input = input("Please enter a number: ")

            # attempt to convert the input to a float
            # this will raise a ValueError if input is not numeric
            number = float(user_input)

        except ValueError:
            # if a ValueError is raised, the input is not a valid number
            raise NotNumericError("The input is not a valid number.")
        
        except NotNumericError as e:
            # handle the custom NotNumericError exception
            print(f"Error: {e}")
        
        else:
            # if no exception is raised, the input is valid
            print(f"Thank you! You entered a valid number: {number}")
            break  # exit the loop after valid input

        finally:
            # indicate the end of this iteration
            print("End of iteration. Let's try again.")

# run the main function
main()
