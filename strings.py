def main():
    # Example string
    example_string = "Hello, Python programmers!"
    
    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for cha in example_string:
        print(cha)

    # TODO: Find and print the character with the minimum ASCII value in the string
    min_cha = min(example_string)
    print("\nCharacter with the minimum ASCII value:", min_cha)

    # TODO: Find and print the character with the maximum ASCII value in the string
    max_cha = max(example_string)
    print("\nCharacter with the maximum ASCII value:", max_cha)

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    index_of_o = example_string.find('o')
    print("\nIndex of 'o':", index_of_o)

    # TODO: Convert the string into a list of characters and print the list
    cha_list = list(example_string)
    print("\nConverting string to a list of characters:", cha_list)

    # TODO: Count and print the number of occurrences of 'o' in the string
    count_of_o = example_string.count('o')
    print("\nCount of 'o' in the string:", count_of_o)

# Calls the main function
main()
