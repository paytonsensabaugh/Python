time_slots = ["Morning", "Midday", "Afternoon", "Evening"] #times
heart_rates = [] #empty heart rate list 
total_heart_rate = 0 #adds to get the total heart rate 
for slot in time_slots: #loop
    heart_rate = int(input(f"Enter your heart rate (in BPM) in the {slot}: ")) #user enters their heart rates throughout the day 
    
    heart_rates.append([slot, heart_rate]) #appending a sublist (a list inside another list)
    
    total_heart_rate += heart_rate #adds the heart rate to get the total heart rate

    average_heart_rate = total_heart_rate / len(time_slots) #calculates the average heart rate by dividing the total sum of heart rates by the number of time slots

print(f"Average heart rate today: {average_heart_rate:.2f} BPM") #calculates the total heart rate 
