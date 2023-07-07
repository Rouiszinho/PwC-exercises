# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Remova todos os caracteres duplicados da string abaixo:

entrada = input("Input: ")                    # Solicita a entrada do usuário
guardaCaractere = []

for caractere in entrada:                     # Checando se não há caracteres repetidos
    if caractere not in guardaCaractere:
        guardaCaractere.append(caractere)
textoFinal = "".join(guardaCaractere)         # Unindo o array para uma frase

print("Output:", textoFinal)                  # Imprimindo a frase
