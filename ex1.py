# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:

entrada = input("Input: ")                       # Pedindo a entrada do usuário
guardaEntrada = list(reversed(entrada.split()))  # Listando as palavras da ultima posição à primeira
entradaUnida = " ".join(guardaEntrada)           # Unindo a lista para uma frase
print("Output:", entradaUnida)                   # Imprimindo a ordem reversa da entrada
