# lists 

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

steps = []

for day in days:
    while True:
        try:
            num_steps = int(input(f"How many steps did you take on {day}? "))
            if num_steps < 0:
                print("Positive Number Only Please.")
            else:
                steps.append(num_steps)
                break
        except ValueError:
            print("Whole Number Only Please.")

# https://www.w3schools.com/python/python_try_except.asp 
# https://www.w3schools.com/python/python_for_loops.asp

for i in range(len(days)):
    print(f"you took {steps[i]} on {days[i]}")

total_steps = sum(steps)
print(f"\nThe total number of steps: {total_steps}")

average = round(total_steps / len(steps))
print(f"\nThe average number of steps: {average}")