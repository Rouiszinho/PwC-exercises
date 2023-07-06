# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Encontre a substring palindroma mais longa na string abaixo:

import re
import unicodedata

entrada = input("Input: ")
normalizado = unicodedata.normalize('NFD', entrada)
texto = re.compile(r'[a-zA-Z]')
correspondencia = texto.finditer(normalizado.lower())
entradaInversa =''.join(reversed(normalizado.lower()))
correspondenciaInversa = texto.finditer(entradaInversa)





