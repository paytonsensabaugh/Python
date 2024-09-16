# empty list
names = []

# enter names
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

# prints the names
print("\nOriginal list of names:")
print(names)

# bubble sort
names.sort ()
print (names)

# prints sorted list 
print("\nSorted list of names (ascending order):")
print(names)

# reverses the list
names.reverse()

# Prints the list
print("\nReversed list of names:")
print(names)
