def main():
    # create an empty list 
    book_titles = []

    # use a while loop to collect 10 book titles from the user
    while len(book_titles) < 10:
        # prompt the user to enter a book title
        title = input("Enter a book title: ")

        # capitalize the first letter of each word in the title 
        book_titles.append(title.title())

    # create a sorted list of the book titles 
    sorted_titles = sorted(book_titles)

    # display each title from the sorted list 
    print("\nHere are your book titles in alphabetical order:")
    for title in sorted_titles:
        print(title)

# call the main function 
main()
