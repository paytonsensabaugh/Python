#divisible by 7 
#def main defines a function called main that you can then use in your script.
def main(): 
    for number in range(1, 301): #his loop iterates through numbers starting from 1 up to 300 (inclusive).
        if number % 7 == 0: #The modulus operator % computes the remainder of number divided by 7. If the remainder is 0, the number is divisible by 7.
            print(number) #If the condition is true, the number is printed.

if __name__ == "__main__":   #used to determine whether the current script is being run as the main program or if it is being imported as a module into another script
    main()
