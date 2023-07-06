# Code by Luiz / Rouiszinho
#
# ENUNCIADO:
# Encontre a substring palindroma mais longa na string abaixo:

import re

entrada = input("Input: ")
texto = re.compile(r'[a-zA-Z]')
correspondencia = texto.finditer(entrada.lower())
for i in correspondencia:
    print(i)