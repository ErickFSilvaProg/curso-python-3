"""
Exercício: Exiba os índices da lista.

Exemplo:
    
    0 Maria
    1 Helena
    2 Luiz
"""

# Primeira forma:
lista = ["Maria", "Helena", "Luiz"]
count = 0

for pessoa in lista:
    print(f"{count} {pessoa}")
    
    count += 1


# Segunda forma:
lista2 = ["João", "Antônio", "Erick", "Gustavo", "Pedro", "Miguel"]
lista2.append("Lucas")
indices = range(len(lista2))

print(indices)

for indice in indices:
    print(indice, lista2[indice], type(lista2[indice]))
