from datetime import datetime

#main function 
def main():
    try:
        #asks the user for their birth year month and day
        year = int(input("What year were you born? "))  # Get the birth year as an integer
        month = int(input("What month were you born (as a number, e.g., May would be 5)? "))  # Get the birth month as an integer
        day = int(input("What day of the month were you born? "))  # Get the birth day as an integer
        
        #creates a datetime for the users birthday
        birthday = datetime(year, month, day)
        
        #displays the users birthday in YYYY-MM-DD format
        print("Your birthday is:", birthday.year, "/", birthday.month, "/", birthday.day)  

        
        #gets the current date and time
        today = datetime.now()
        
        #calculates the difference in the days between today and the birthday
        age_delta = today - birthday
        total_days = age_delta.days
        
        #calculates the age in years
        years = total_days // 365  # Divide by 365 to get whole years
        
        #calculates the remaining days after years
        remaining_days = total_days % 365
        
        #calculates the age in months
        months = remaining_days // 30  # Approximate months (30 days per month)
        
        #calculates the age in weeks
        weeks = total_days // 7  # Divide by 7 to get whole weeks
        
        #calculates the remaining days after weeks
        remaining_days_after_weeks = total_days % 7
        
        #calculates the hours and minutes
        hours = total_days * 24
        minutes = total_days * 24 * 60
        
        #results
        print(f"Difference is {total_days} days")
        print(f"You are {years} years, {months} months, and {remaining_days_after_weeks} days old.")
        print(f"Or approximately {weeks} weeks old.")
        print(f"Or approximately {hours} hours old.")
        print(f"Or approximately {minutes} minutes old.")
    
    except ValueError:
        #handles any input errors
        print("Please enter valid integers for the year, month, and day.")

#calls the function
main()
