"""
Exercício: Exiba os índices da lista.

Exemplo:
    
    0 Maria
    1 Helena
    2 Luiz

"""


# Primeira forma:
lista = ["Maria", "Helena", "Luiz"]
i = 0

for pessoa in lista:
    print(f"{i} {pessoa}")
    i += 1
print()


# Segunda forma:
lista2 = ["João", "Antônio", "Erick", "Gustavo", "Pedro"]
lista2.append("Lucas")
lista2.insert(1, "Miguel")

indices = range(len(lista2))

for i in indices:
    print(i, lista2[i])
print()