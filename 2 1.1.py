import random

#generate a random number between 1 and 100
number = random.randint(1, 100)
print("Guess the number between 1 and 100!") #prints the statment 

def main(): #main function
    while True: #loops so if the user inputs a value that is not an integer it will ask for reentry and if they get the number wrong
        try:
            #user's guess
            guess = int(input("Enter your guess: "))
            difference = abs(guess - number)

            #tells the user if they got the number or how "hot" and "cold" they are
            if difference == 0:
                print("Congratulations! You've guessed the correct number!")
                break
            elif difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")

        except ValueError: #if users inputs a invalid integer
            print("Please enter a valid integer.")

main() #calls the main function
