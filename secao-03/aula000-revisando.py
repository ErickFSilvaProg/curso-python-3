"""
- Fatiamento de strings:

    Índices:             012345678
    String:              Olá mundo
    Índices negativos:  -987654321

Fatiamento [i:f:p] [início:fim:posição]
Obs.: A função 'len' retorna a quantidade de caracteres da string.

"""

#          [012345678]
variavel = "Olá mundo"
#         [-987654321]

print("- Iterando string:")
print(variavel)
print(variavel[4])
print(variavel[-5])
print()

print("- Fatiamento de string: Índices positivos.")
print(variavel[4:9]) # Declarando o início e o fim do fatiamento.
print(variavel[4:]) # Declarando apenas o início. O fatiamento irá até o fim.
print(variavel[0:5])
print(variavel[:5]) # Declarando apenas o final. O fatiamento será do início a posição informada.
print()

print("- Fatiamento de string: Índices negativos.")
print(variavel[-8:-2])
print()

print("- Função len(): Conta os caracteres.")
print(len(variavel))
print(len(variavel[3]))
print()

