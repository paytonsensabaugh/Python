def main():
    # predefined list of top 10 performing artists
    top_artists = [
        "The Beatles", "Madonna", "Elton John", "Elvis Presley", 
        "Mariah Carey", "Stevie Wonder", "Janet Jackson", 
        "Michael Jackson", "Whitney Houston", "Rihanna"
    ]

    # function to replace an artist in the list
    def replace_artist():
        try:
            # ask the user for the index to replace
            index = int(input("Enter the index of the artist to replace (0-9): "))
            
            # ask for the new artist name
            new_artist = input("Enter the new artist name: ").strip()

            # replace the artist at the specified index
            top_artists[index] = new_artist

            # print the updated list
            print("\nUpdated list:")
            print(top_artists)
        
        except ValueError:
            print("Error: Invalid input. Please enter a valid number for the index.")
        except IndexError:
            print("Error: Index out of range. Please enter an index between 0 and 9.")
        except Exception as e:
            print(f"An input error occurred: {e}")

    # call the function
    replace_artist()

# call the main function 
main()
