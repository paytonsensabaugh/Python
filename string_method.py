# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
string1 = "python"
capitalized_string1 = string1.capitalize()
print("Capitalized:", capitalized_string1)  # Output: Python

# TODO: Use the center() method to center the string in a string of specified width
string2 = "python"
centered_string2 = string2.center(20)
print("Centered:", centered_string2)  # Output: "       python        "

# TODO: Use the endswith() method to check if the string ends with a specified substring
string3 = "python"
ends_with_on = string3.endswith("on")
print("Ends with 'on':", ends_with_on)  # Output: True

# TODO: Use the find() method to find the first occurrence of a substring in the string
string4 = "python"
find_th = string4.find("th")
print("Position of 'th':", find_th)  # Output: 2

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
string5 = "python3"
is_alphanumeric = string5.isalnum()
print("Is alphanumeric:", is_alphanumeric)  # Output: True

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
string6 = "python"
is_alpha = string6.isalpha()
print("Is alphabetic:", is_alpha)  # Output: True

# TODO: Use the islower() method to check if all characters in the string are lowercase
string7 = "python"
is_lower = string7.islower()
print("Is lowercase:", is_lower)  # Output: True

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
string8 = " "
is_space = string8.isspace()
print("Is all whitespace:", is_space)  # Output: True

# TODO: Use the isupper() method to check if all characters in the string are uppercase
string9 = "PYTHON"
is_upper = string9.isupper()
print("Is uppercase:", is_upper)  # Output: True

# TODO: Use the join() method to join elements of an iterable with the string as the separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
joined_string = separator.join(iterable1)
print("Joined string:", joined_string)  # Output: Python-is-fun

# TODO: Use the lower() method to convert all characters in the string to lowercase
string10 = "PYTHON"
lowercase_string10 = string10.lower()
print("Lowercase:", lowercase_string10)  # Output: python

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
string11 = " python"
stripped_string11 = string11.lstrip()
print("Stripped leading spaces:", stripped_string11)  # Output: "python"

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
string12 = "python "
stripped_string12 = string12.rstrip()
print("Stripped trailing spaces:", stripped_string12)  # Output: "python"

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
string13 = "I love python"
replaced_string13 = string13.replace("python", "snake")
print("Replaced string:", replaced_string13)  # Output: I love snake

# TODO: Use the rfind() method to find the highest index of a substring
string14 = "python"
highest_index_n = string14.rfind("n")
print("Highest index of 'n':", highest_index_n)  # Output: 5

# TODO: Use the split() method to split the string at a specified separator
string15 = "python-is-fun"
split_string15 = string15.split("-")
print("Split string:", split_string15)  # Output: ['python', 'is', 'fun']

# TODO: Use the startswith() method to check if the string starts with a specified substring
string16 = "python"
starts_with_py = string16.startswith("py")
print("Starts with 'py':", starts_with_py)  # Output: True

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
string17 = " python "
stripped_string17 = string17.strip()
print("Stripped spaces:", stripped_string17)  # Output: "python"

# TODO: Use the swapcase() method to swap the case of all characters in the string
string18 = "Python"
swapped_case_string18 = string18.swapcase()
print("Swapped case:", swapped_case_string18)  # Output: pYTHON

# TODO: Use the title() method to convert the first character of each word to uppercase
string19 = "python is fun"
title_case_string19 = string19.title()
print("Title case:", title_case_string19)  # Output: Python Is Fun

# TODO: Use the upper() method to convert all characters in the string to uppercase
string20 = "python"
uppercase_string20 = string20.upper()
print("Uppercase:", uppercase_string20)  # Output: PYTHON
