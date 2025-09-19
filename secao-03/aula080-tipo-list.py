"""
# Listas em Python: (São semelhantes aos 'arrays' em outras linguagens.)

    Tipo list - Mutável
    Suporta vários valores de qualquer tipo.
    Conhecimentos reutilizáveis - Índices e fatiamento.
    
    - Métodos úteis:

        append, insert, pop, del, clear, extend, ...

"""

# - Exemplo de string:
#         12345
#        -54321
string = "ABCDE"
print(f"{len(string)} caracteres do tipo string.\n")


# - Exemplos criação de lista:

# Exemplo 1: Menos utilizado.
lista_1 = list()
print(type(lista_1), lista_1)
print(bool(lista_1)) # Lista vazia retorna 'False'
print()

# Exemplo 2: Mais utilizado.
#        0    1     2              3    4
#       -5   -4    -3             -2   -1
lista = [123, True, "Programador", 1.2, ["HTML", "CSS", "JS", "DJANGO", "API"]]

print(lista)
print(lista[2].upper(), type(lista[2]))

lista[2] = "Programador Python"
print(lista[2])
print()

for itens in lista:
    print(itens)
print()

for sub_itens in lista[4]:
    print(sub_itens)