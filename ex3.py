# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Encontre a substring palindroma mais longa na string abaixo:

import re                                                              
import unicodedata

def normalizacao(frase):
    normalizado = unicodedata.normalize('NFD', frase)
    texto = re.compile(r'[a-z]')
    correspondencia = list(texto.finditer(normalizado.lower()))
    juncao = ""
    for i in correspondencia:
        juncao += i.group()

    return juncao

def palindromo(frase):
    palindro=True
    for i in range(0, len(frase)):
        if(frase[i] != frase[len(frase)-i-1]):
            palindro = False
                
    if palindro and len(frase) > 1:
        return frase
    
frase = input("Input: ")
frase = normalizacao(frase)
maior = ""
for i in range(0, len(frase)):
    for j in range(i, len(frase)):
        p = palindromo(frase[i:j+1])
        
        if(p and len(p) > len(maior)):
            maior = p
            
print(maior)
