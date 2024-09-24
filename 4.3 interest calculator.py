#interest calculator
#Simple interest is calculated using the formula:
#Simple Interest = (Principal Amount × Rate of Interest × Time) / 100

def calculator_interest(principle, rate, time):
    total = principal * rate * time / 100 
    return total


principal = int(input("Enter the principal amount (the initial sum of money): "))
rate = int(input("Enter the rate of interest as a whole number (5% would be 5): "))
time = int(input("The time the money is invested or borrowed for, in years: "))

interest = calculator_interest(principal, rate, time)

print(f"The simple interest for a principal amount of {principal} at an interest rate of {rate}% over a period of {time} years is: {interest}")
