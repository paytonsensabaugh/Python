# exmaple 

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width
# print(f"The area of the rectangle is {area:.2f}")

# Housing rent 
months = float(input("Enter how many months a year do you pay for rent. Ex every month(12), every 6 months(2): ")) 
spending = float(input("Enter your yearly spending for housing.: "))
housingyear = months * spending 
print(f"The yearly spending is {housingyear:.2f}")

# Groceries  
times = float(input("Enter how many times a month you go grocery shopping: "))
spending = float(input("Enter on average how much you spend on groceries: "))
groceriesyear = times * spending * 12
print(f"The yearly spending on groceries is {groceriesyear:.2f}")

# Transportation (car)
months = float(input("Enter how many times a month do you fill up your tank: "))
spending = float(input("Enter how much does an empty tank cost to fill: "))
caryear = months * spending * 12
print(f"The yearly cost of gas on empty tanks is {caryear:.2f}")

# Health Care 
months = float(input("Enter how much your monthly health care is: "))
healthyear = months * 12
print(f"The monthly health care bill is {healthyear:.2f}")

# Personal Care 
months  = float(input("Enter how much a month you spend on personal care items: "))
personalyear = months * 12
print(f"The yearly cost of your personal care is {personalyear:.2f}")

# Clothing 
months = float(input("Enter how much money a month you spend on clothing items: "))
clothingyear =  months * 12
print(f"The yearly spending on clothing is {clothingyear:.2f}")

# Debt
# this one took me like an hour, I could not figure out what was going wrong
# Im pretty sure I did this assingment right but not 100% sure 
balance = float(input("Enter the remaining balance of your debt: "))
interest = float(input("Enter your intest rate(in whole number): "))
totalinterest = balance * interest 
total = totalinterest + balance
length = float(input("Enter the remaining time you have to pay on your loan(months): "))
debtyear = total / length 
print(f"The yearly payment for your loan is {debtyear:.2f}")
