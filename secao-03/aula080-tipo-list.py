"""
- Listas em Python: (São semelhantes aos 'arrays' em outras linguagens.)

Tipo list - Mutável
Suporta vários valores de qualquer tipo.

Conhecimentos reutilizáveis - Índices e fatiamento.
"""

#         01234
#        -54321
string = "ABCDE"
print(string[2])


# Como criar listas:
modelo_lista_1 = list() # Lista vazia
modelo_lista_2 = [] # Lista vazia

print(modelo_lista_1, type(modelo_lista_1))
print(modelo_lista_2, type(modelo_lista_2))


lista_1 = [123, True, "Luiz Otávio", 1.2, ["lista", "interna"]]
print(lista_1)
print(lista_1[0])
print(lista_1[1])
print(lista_1[2])
print(lista_1[3])
print(lista_1[4][0])
print(lista_1[4][1])

lista_1[2] = "Erick Ferreira"
print(lista_1)