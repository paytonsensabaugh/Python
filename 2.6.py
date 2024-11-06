def main():
    # create an empty list to store the flower names
    flowers = []

    # collect flower names from the user
    print("Enter flower names one by one. Type 'done' when you're finished.")
    while True:
        flower = input("Enter a flower name: ").strip()  # gets user input and remove extra spaces
        
        if flower.lower() == 'done':  # checks if the user is done entering names
            break
        
        if flower:  # ensure that the input is not empty
            flowers.append(flower)
        else:
            print("Invalid input. Please enter a valid flower name.")
    
    # sorts the list of flowers 
    flowers.sort()

    # prints the sorted flower list
    print("\nSorted Flower List:")
    for index, flower in enumerate(flowers, start=1):
        print(f"{index}. {flower}")
    
    # allows the user to search 
    search_flower = input("\nEnter a flower name to search for: ").strip()
    try:
        if search_flower in flowers:
            print(f"{search_flower} is found in the list.")
        else:
            print(f"{search_flower} is not found in the list.")
    except Exception as e:
        print(f"An error occurred during search: {e}")
    
    # allows the user to access a specific flower
    while True:
        try:
            flower_number = int(input("\nEnter the number of the flower you want to access (1 to {}): ".format(len(flowers))))
            # adjust for zero-based indexing 
            if 1 <= flower_number <= len(flowers):
                print(f"The flower at position {flower_number} is: {flowers[flower_number - 1]}")
                break  # exits the loop 
            else:
                print(f"Please enter a number between 1 and {len(flowers)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Error: That number is out of range.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# calls the main function 
main()
