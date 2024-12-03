#No Magic Numbers
NegativeOne = -1
Hundred, Zero = 100, 0
def main():
    # Triple-quoted string for favorite paragraph
    paragraph = """First autumn morning
the mirror I stare into
shows my father's face."""
    # A - Mirror the string
    def mirror_string(text):
        return text + text[::NegativeOne]
    # B - Remove all occurrences of a given letter
    def remove_letter(text, letter):
        return text.replace(letter, "")
    # C - Count alphabetic characters and occurrences of 'e'
    def char_num(text):
        alphabetic = sum(1 for char in text if char.isalpha())
        e_count = text.lower().count('e')
        percentage = (e_count / alphabetic) * Hundred if alphabetic > Zero else Zero
        return f"Your text contains {alphabetic} alphabetic characters, of which {e_count} ({percentage:.1f}%) are 'e'."
    # D - Count occurrences of any character
    def char_num_generic(text, char):
        alphabetic = sum(1 for c in text if c.isalpha())
        char_count = text.lower().count(char.lower())
        percentage = (char_count / alphabetic) * Hundred if alphabetic > Zero else Zero
        return f"Your text contains {alphabetic} alphabetic characters, of which {char_count} ({percentage:.1f}%) are '{char}'."
    # E - Check if a word has no 'e'
    def no_e(word):
        return 'e' not in word.lower()
    # F - Check if a word has no specified character
    def no_char(word, char):
        return char.lower() not in word.lower()
    # G - Words with no 'e' and percentage
    def words_no_e(text):
        words = text.split()
        no_e_words = [word for word in words if no_e(word)]
        percentage = (len(no_e_words) / len(words)) * Hundred if words else Zero
        return no_e_words, percentage
    # H - Avoids forbidden letters
    def avoids(word):
        forbid = input("Enter forbidden letters: ")
        splitwords = word.split()
        for i in splitwords:
            if all(letter not in i for letter in forbid):
                print(i)
        return 'Those were all the words without the forbidden letters!'
    # I - Uses only specific letters
    def uses_only(word, allowed_letters):
        allowed_letters = set(allowed_letters) | {" "}
        return set(word).issubset(allowed_letters) and set(allowed_letters - {" "}).issubset(set(word))
    # J - Uses all required letters
    def uses_all(word, required_letters):
        return all(char in word for char in required_letters)
    # K - Abecedarian words
    def is_abecedarian(word):
        return list(word) == sorted(word)
    # L - Find the index of a character
    def find(text, char):
        return text.find(char)
    # M - Find index starting from a position
    def find_from(text, char, start_index):
        return text.find(char, start_index)
    # N - Check if words are sorted
    def is_sorted(text):
        words = text.split()
        return words == sorted(words)
    # O - Check if two words are anagrams
    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    # P - Check for duplicate characters
    def has_duplicates(text):
        return len(set(text)) != len(text)
    # Q - Remove duplicate characters
    def remove_duplicates(text):
        return ''.join(dict.fromkeys(text))
    #Function calls:
    print('Paragraph:', paragraph)
    #Part A
    print("\nA:", mirror_string(paragraph))
    #Part B
    print("\nB:")
    noneofthat = input('Input one letter to remove it from the paragraph: ')
    print(remove_letter(paragraph, noneofthat))
    #Part C
    print("\nC:", char_num(paragraph))
    #Part D
    print("\nD:", char_num_generic(paragraph, 'o'))
    #Part E
    print("\nE:")
    eword = input('Input any word but try with no e\'s: ')
    print('The letter had no e\'s: ', no_e(eword))
    #Part F
    print("\nF:")
    secondstopper = input('Input a letter and we\'ll check if it\'s in the last word: ')
    print('The word did not have this new letter:', no_char(eword, secondstopper))
    words, percentage = words_no_e(paragraph)
    #Part G
    print("\nG:", words, f"{percentage:.1f}% words have no 'e'")
    #Part H
    print("\nH:")
    print(avoids(paragraph))
    #Part I
    print("\nI:")
    theletters = input('Input some letters to use for the next prompt: ')
    usesonlyin = input('Try to make a sentence with ony the prior letters: ')
    if uses_only(usesonlyin, theletters):
        print('You got it!')
    else:
        print('Not there yet you used other letters!')
    #Part J
    print("\nJ:")
    PartJWord = input('Make a word/phrase that uses aeiou: ')
    print('You used aeiuo?: ', uses_all(PartJWord, "aeiou"))
    #Part K
    print("\nK:")
    PartKWord = input('Make a word/phrase that has its letter appear in alphebetical order: ')
    print('Are the letters alphebetical:', is_abecedarian(PartKWord))
    #Part L
    print("\nL:")
    findthisone = input('Input a letter you want to find in the paragraph: ')
    print('It\'s index is:', find(paragraph, findthisone))
    #------Part M
    print("\nM:")
    Whatchar = input('What letter do you want to find again?: ')
    WhatIndex = int(input('What index do you want to start looking?: '))
    print('The index of what you wanted to find is:', find_from(paragraph, Whatchar, WhatIndex))
    #-------Part N
    print("\nN:")
    NString = input('Create a string with words in ascending order: ')
    print('Is it sorted:', is_sorted(NString))
    #Part O
    print("\nO:")
    firstOWord = input('Input a word: ')
    secondOWord = input('Now try to put in that word\'s anagram: ')
    print('Are the two anagram of each other?:', is_anagram(firstOWord, secondOWord))
    #Part P
    print("\nP:")
    dupliWord = input('Enter any word: ')
    print('Does the word have any duplicate letters?:', has_duplicates(dupliWord))
    #part Q
    print("\nQ:")
    secondDupli = input('Try to input a word with multiple of the same letters: ')
    print('The word without duplicates:', remove_duplicates(secondDupli))
# Execute the program
main()
