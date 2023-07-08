# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Verifique se a string é um anagrama de um palindromo:

import re                                                              
import unicodedata

def normalization(phrase):                                   # Getting only the text characters 
    normalized = unicodedata.normalize('NFD', phrase)        # Normalizes the sentence by removing accents
    text = re.compile(r'[a-z]')                              # Defines a regular expression to find only text characters
    correspondence = list(text.finditer(normalized.lower())) # Find matches in the phrase
    junction = ""
    for character in correspondence:
        junction += character.group()                        # Concatenates to letters

    return junction

phrase = input("Input: ")                                    # Asks for user input
phrase = normalization(phrase)                               # Normalizes the sentence
reverseSentence = ''.join(reversed([*phrase]))               # Inverts the normalized sentence
print("Output:", phrase == reverseSentence)                  # Prints if the normalized sentence is equal to its inverse


