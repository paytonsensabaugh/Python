
grade = float(input("Enter your numeric grade (0-100): "))
        
if 0 <= grade <= 100:
        letter_grade =(grade)
        print(f"Your letter grade is: {letter_grade}")
else:
        print("Error: The grade must be between 0 and 100.")
    
if 90 <= grade <= 100:
    print("A") 
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
elif 60 <= grade < 70:
    print("D")
elif 0 <= grade < 60:
    print("F")
