#The Nato alphabet in a dict
nato_alphabet = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

#The spelling program
def spell_word():
    user_word = input("Please enter a word: ") #User enters a word
    user_word = user_word.upper()  # Converts to uppercase to match dictionary keys

    print("NATO Phonetic Spelling:")
    for letter in user_word:
        if letter in nato_alphabet:  # Check if the letter is in the dictionary
            print(nato_alphabet[letter]) # Prints the word in the nato
        else:
            print(f"'{letter}' is not a valid letter.")

#I know you dont need this but I wasnt sure if you wanted it to be named main or not. The assignment says to call main. 
#I know I can simply just delete this and type "spell_word()" but than it isnt named main
# Like I said I wasnt sure so I just added it. 
def main():
    spell_word()

# runs the fuction
main()
#spell_word()