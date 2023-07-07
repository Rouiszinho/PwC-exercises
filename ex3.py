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


