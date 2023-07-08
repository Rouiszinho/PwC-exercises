# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Remova todos os caracteres duplicados da string abaixo:

userInput = input("Input: ")                    # Asks for user input
characterGuard = []

for character in userInput:                     # Checking if there are no repeated characters
    if character not in characterGuard:
        characterGuard.append(character)
finalText = "".join(characterGuard)             # Joining the array to a sentence

print("Output:", finalText)                     # Printing the sentence
