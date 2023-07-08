# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Remova todos os caracteres duplicados da string abaixo:

while True:
    userInput = input("Input: ")                    # Asks for user input
    characterGuard = []

    for character in userInput:                     # Checking if there are no repeated characters
        if character not in characterGuard:
            characterGuard.append(character)
    finalText = "".join(characterGuard)             # Joining the array to a sentence

    print("Output:", finalText)                     # Printing the sentence
    user_input = input("Press Enter to close or type 'exit' to exit: ")
    if user_input == "":
        break                                       # Exit the loop and exit the program
    elif user_input.lower() == "exit":
        exit()                                      # Terminate the program immediately
