# Simple Python program to calculate the square of a number

def square_number():
    while True: #this loops until a valid response is imputed
        try: #tests the code for errors 
            number = input("Enter a number to square: ")
            squared_number = int(number) ** 2
            print(f"The square of {number} is {squared_number}.")
        except ValueError: #handles the error from an invalid input
            print("That's not a valid number. PLease try again")

square_number()