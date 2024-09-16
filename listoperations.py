#listoperations 
available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #seats

while True:
    print("\nSeats:", available_seats) #list of seats
 
    seat_choice = input("\nEnter the seat you want: ") 

    seat_choice = int(seat_choice) #user enters the seat they want to buy

    if seat_choice == 0: # how user exits the buying
        print("\nThank you")
        break

    if seat_choice in available_seats: #user buys the seat and than it removes the bought seat from the list 
        available_seats.remove(seat_choice)
        print(f"Seat {seat_choice} has been bought!")
    else:
        print("Seat is either sold or non-exsistant.") #user trys to buy a seat that is either sold out or not listed 
    
    if len(available_seats) == 0: # if all the seats are sold
        print("\nSold out.")
        break


    
