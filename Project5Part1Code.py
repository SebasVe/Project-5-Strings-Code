#No Magic Numbers
NegativeOne, Zero, Two, ThirtyFive, TwentyFive, Seventy = -1, 0, 2, 35, 25, 70
def main():
    # Part I: User input
    full_name = input("Please enter your full name: ")
    # Function 1: Display the number of characters
    def count_characters(name):
        return len(name)
    # Function 2: Display the last character
    def last_character(name):
        return name[NegativeOne]
    # Function 3: Find the first occurrence of 'e'
    def first_e_position(name):
        return name.find('e') if 'e' in name else Zero
    # Function 4: Count the number of words
    def count_words(name):
        return len(name.split())
    # Function 5: Get the first word
    def first_word(name):
        return name.split()[Zero]
    # Function 6: Count the number of vowels
    def count_vowels(name):
        vowels = "aeiouAEIOU"
        return sum(1 for char in name if char in vowels)
    # Function 7: Capitalize all vowels and lowercase consonants
    def capitalize_vowels(name):
        vowels = "aeiouAEIOU"
        return ''.join(char.upper() if char in vowels else char.lower() for char in name)

    # Function 8: Center the string with ~ and +
    def centered_string(name):
        return f"{'+'*ThirtyFive}{'~'*TwentyFive}{name}{'~'*TwentyFive}{'+'*ThirtyFive}"

    # Function 9: Split the string in half with *
    def split_string(name):
        half = len(name) // Two
        return f"{name[:half]}{'*'*Seventy}{name[half:]}"
    # Call and display the results of each function
    print("Your name is {} characters long.".format(count_characters(full_name)))
    print("The last character is: {}".format(last_character(full_name)))
    print("The first 'e' is at position {}.".format(first_e_position(full_name)))
    print("Your name has {} words.".format(count_words(full_name)))
    print("Your first name is {}.".format(first_word(full_name)))
    print("Your name contains {} vowels.".format(count_vowels(full_name)))
    print("Your name with uppercase vowels is: {}".format(capitalize_vowels(full_name)))
    print(centered_string(full_name))
    print(split_string(full_name))
# Execute the program
main()
