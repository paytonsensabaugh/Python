# Constants for conversions
POUNDS_TO_KILOGRAMS = 0.453592
INCHES_TO_METERS = 0.0254


def get_valid_number(prompt):
        try:
            user_input = input(prompt)  # Ask for user input
            number = float(user_input)  # Attempt to convert to float
            return number  # Return the valid number

def main():
    # Get weight in pounds from user
    weight_pounds = get_valid_number("Please enter your weight in pounds: ")
    # Get height in inches from user
    height_inches = get_valid_number("Please enter your height in inches: ")

    # Convert weight and height to metric units
    weight_kg = weight_pounds * POUNDS_TO_KILOGRAMS  # Convert pounds to kilograms
    height_m = height_inches * INCHES_TO_METERS  # Convert inches to meters

    # Calculate BMI
    bmi = weight_kg / (height_m * height_m)  # BMI formula

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    # Output the results
    print(f"Your BMI is: {bmi:.2f}")  # Display BMI rounded to two decimal places
    print(f"BMI Category: {category}")  # Display the corresponding category


# Directly call the main function
main()
