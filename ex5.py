# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Verifique se a string é um anagrama de um palindromo:

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

frase = input("Input: ")                                # Pedindo a entrada do usuário
frase = normalizacao(frase)
fraseReversa = ''.join(reversed([*frase]))
print("Output:", frase == fraseReversa)


