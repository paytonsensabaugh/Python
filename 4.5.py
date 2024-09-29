def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive step: n! = n * (n-1)!
    # Used for the math that gets your integer 
    return n * factorial(n - 1)

def main():
    # Prompts the user for a non-negative integer
    user_input = input("Please enter a non-negative integer: ")

    # Converts the users input to an integer from a string
    n = int(user_input)

    # Ensure that the users input is non-negative
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return

    # Calls the factorial function and print the result the user types 
    result = factorial(n)
    print(f"The factorial of {n} is {result}.")

# Calls the main function that runs the program
main()
