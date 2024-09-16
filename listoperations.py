available_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while True:
    print("\nSeats:", available_seats) 
 
    seat_choice = input("\nEnter the seat you want: ")

    seat_choice = int(seat_choice)

    if seat_choice == 0: 
        print("\nThank you")
        break

    if seat_choice in available_seats: 
        available_seats.remove(seat_choice)
        print(f"seat {seat_choice} has been bought!")
    else:
        print("Seat is either sold or non-exsistant.")
    
    if len(available_seats) == 0:
        print("\nSold out.")
        break


    
