def get_letter_grade(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    elif 0 <= grade < 60:
        return 'F'
    else:
        return None

def main():
    try:
        grade = float(input("Enter your numeric grade (0-100): "))
        
        if 0 <= grade <= 100:
            letter_grade = get_letter_grade(grade)
            print(f"Your letter grade is: {letter_grade}")
        else:
            print("Error: The grade must be between 0 and 100.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric grade.")

if __name__ == "__main__":
    main()