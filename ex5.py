# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Verifique se a string é um anagrama de um palindromo:

import re                                                              
import unicodedata

def normalizacao(frase):                                # Obtendo somente os caracteres de texto 
    normalizado = unicodedata.normalize('NFD', frase)   # Normaliza a frase removendo acentos
    texto = re.compile(r'[a-z]')                        # Define uma expressão regular para encontrar somente caracteres de texto
    correspondencia = list(texto.finditer(normalizado.lower()))  # Encontra as correspondências na frase
    juncao = ""
    for i in correspondencia:
        juncao += i.group()                             # Concatena as letras

    return juncao

frase = input("Input: ")                                # Solicita a entrada do usuário
frase = normalizacao(frase)                             # Normaliza a frase
fraseReversa = ''.join(reversed([*frase]))              # Inverte a frase normalizada
print("Output:", frase == fraseReversa)                 # Imprime se a frase normalizada é igual à sua inversa


