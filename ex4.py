# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Coloque em maiúscula a primeira letra de cada frase na string:


frase = input("Input: ")
frase = [*frase]
acentos = "?!."

for i in range(0, len(frase)):
    
    if i == 0:
        frase[i] = frase[i].upper()
    elif i == len(frase)-1:
        break
    if frase[i] in acentos:
        if frase[i+1] == ' ':
            frase[i+2] = frase[i+2].upper()
        else:
            frase[i+1] = frase[i+1].upper()
frase = ''.join(frase)
print("Output: ", frase)