# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:

while True:
    userInput = input("Input: ")               # Ask for user input
    entryGuard = reversed(userInput.split())   # Listing words from last to first position
    joinedEntry = " ".join(entryGuard)         # Joining the list for a sentence
    print("Output:", joinedEntry)              # Printing input reverse order
    user_input = input("Press Enter to close or type 'exit' to exit: ")
    if user_input == "":
        break                                  # Exit the loop and exit the program
    elif user_input.lower() == "exit":
        exit()                                 # Terminate the program immediately

