# empty list, says to have the user enter the names
names = []

# enter names, user enters the names into the terminal
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

# prints the names, prints the names that the user inputed 
print("\nOriginal list of names:")
print(names)

# bubble sort, sorts the names that the user has inputed 
names.sort ()
print (names)

# prints sorted list, prints those names that were sorted 
print("\nSorted list of names (ascending order):")
print(names)

# reverses the list, reverses the list 
names.reverse()

# Prints the list, prints the reversed list
print("\nReversed list of names:")
print(names)
