# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Encontre a substring palindroma mais longa na string abaixo:

import re                                                              
import unicodedata

def normalization(phrase):                                # Getting only the text characters
    normalized = unicodedata.normalize('NFD', phrase)
    text = re.compile(r'[a-z]')
    correspondence = list(text.finditer(normalized.lower())) 
    junction = ""
    for character in correspondence:
        junction += character.group()

    return junction

def palindromo(phrase):                                  # Checking if the sentence is a palindrome
    palindro = phrase == ''.join(reversed([*phrase]))
    if palindro and len(phrase) > 1:
        return phrase
    
phrase = input("Input: ")                                # Asks for user input
phrase = normalization(phrase)                           # Calling the normalization function 
bigger = ""                                              # Creating bigger variable to store bigger palindrome
for i in range(0, len(phrase)):                          # Loop to get character at position i
    for j in range(i, len(phrase)):                      # Loop checking from character i to end of sentence
        p = palindromo(phrase[i:j+1])                    # Calling palindrome inner function passing from i to j+1
        
        if(p and len(p) > len(bigger)):
            bigger = p
            
print("Output", bigger)                                  # Longest palindromic substring printout             
