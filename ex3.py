# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Encontre a substring palindroma mais longa na string abaixo:

import re                                                              
import unicodedata

def normalizacao(frase):                                # Obtendo somente os caracteres de texto 
    normalizado = unicodedata.normalize('NFD', frase)
    texto = re.compile(r'[a-z]')
    correspondencia = list(texto.finditer(normalizado.lower())) 
    juncao = ""
    for i in correspondencia:
        juncao += i.group()

    return juncao

def palindromo(frase):                                  # Conferindo se a frase é um palindromo
    palindro=True
    for i in range(0, len(frase)):
        if(frase[i] != frase[len(frase)-i-1]):
            palindro = False
                
    if palindro and len(frase) > 1:
        return frase
    
frase = input("Input: ")                                # Pedindo a entrada do usuário
frase = normalizacao(frase)                             # Chamando função interna normalizacao 
maior = ""                                              # Craindo variável maior para armazenar o maior palindromo
for i in range(0, len(frase)):                          # Loop para obter o caratere na posição i
    for j in range(i, len(frase)):                      # Loop conferindo do caractere i até o fim da frase
        p = palindromo(frase[i:j+1])                    # Chamando a função interna palindromo passando de i até j+1
        
        if(p and len(p) > len(maior)):
            maior = p
            
print("Output", maior)                                  # Impressão da substring palindrômica mais longa             
