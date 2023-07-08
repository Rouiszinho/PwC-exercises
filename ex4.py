# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Coloque em maiúscula a primeira letra de cada phrase na string:

while True:
    phrase = input("Input: ")                          # Prompts for a phrase for user input
    phrase = [*phrase]                                 # Converts the phrase to a list of characters
    accents = "?!."

    for i in range(0, len(phrase)):

        if i == 0:
            phrase[i] = phrase[i].upper()              # Capitalizes the first character of the sentence
        elif i == len(phrase) - 1:
            break                                      # End the loop before the last character
        if phrase[i] in accents:
            if phrase[i + 1] == ' ':
                phrase[i + 2] = phrase[i + 2].upper()  # Capitalizes the next character if there is a space after the accent
            else:
                phrase[i + 1] = phrase[i + 1].upper()  # Capitalizes the next character
    phrase = ''.join(phrase)                           # Converts the list of characters back to a string
    print("Output:", phrase)                           # Prints the resulting sentence
    user_input = input("Press Enter to close or type 'exit' to exit: ")
    if user_input == "":
        break                                          # Exit the loop and exit the program
    elif user_input.lower() == "exit":
        exit()                                         # Terminate the program immediately