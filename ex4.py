# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Coloque em maiúscula a primeira letra de cada frase na string:


frase = input("Input: ")                    # Solicita uma frase de entrada do usuário
frase = [*frase]                            # Converte a frase em uma lista de caracteres 
acentos = "?!."

for i in range(0, len(frase)):
    
    if i == 0:
        frase[i] = frase[i].upper()         # Capitaliza o primeiro caractere da frase
    elif i == len(frase)-1:
        break                               # Encerra o loop antes do último caractere
    if frase[i] in acentos:
        if frase[i+1] == ' ':
            frase[i+2] = frase[i+2].upper() # Capitaliza o próximo caractere se houver um espaço após o acento
        else:
            frase[i+1] = frase[i+1].upper() # Capitaliza o próximo caractere
frase = ''.join(frase)                      # Converte a lista de caracteres de volta para uma string
print("Output: ", frase)                    # Imprime a frase resultante