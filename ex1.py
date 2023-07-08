# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:

userInput = input("Input: ")                    # Ask for user input
entryGuard = reversed(userInput.split())        # Listing words from last to first position
joinedEntry = " ".join(entryGuard)              # Joining the list for a sentence
print("Output:", joinedEntry)                   # Printing input reverse order
