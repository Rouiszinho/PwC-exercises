# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Remova todos os caracteres duplicados da string abaixo:

entrada = input("Input: ")                    # Pedindo a entrada do usuário
guardaCaractere = []

for caractere in entrada:                     # Checando se não há caracteres repetidos
    if caractere not in guardaCaractere:
        guardaCaractere.append(caractere)


print("Output:", guardaCaractere)                  # Imprimindo a frase
