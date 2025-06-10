"""
- Fatiamento de strings:

Índices:            012345678
String:             Olá mundo
Índices negativos: -987654321

Fatiamento [i:f:p] [início:fim:posição]
Obs.: A função len retorna a quantidade de caracteres da string
"""


#          [012345678]
variavel = 'Olá mundo'
#         [-987654321]

print(variavel[5])
print(variavel[-4])
print('\n')

print(variavel[4:9])
print(variavel[4:])
print('\n')

print(variavel[0:3])
print(variavel[:3])
print('\n')

print(len(variavel)) # Conta os caracteres.

print(variavel[::-1]) # Imprime o resultado invertido.