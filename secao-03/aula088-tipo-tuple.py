# Tipo 'tuple' (tuplas) - É uma lista imutável.

# Lista: Mutável
nomes = ["Maria", "Helena", "Luiz"]
print(nomes)

nomes[1] = "Outro"
print(nomes)


# Tupla: Imutável
nomes2 = "Gustavo", "Pedro", "Miguel"
print(nomes2)

"""
- Retorna o erro: (TypeError: 'tuple' object does not support item assignment)

    nomes2[1] = "Outro"
    print(nomes2)
"""


# Convertento 'lista' em 'tupla'
nomes3 = ["Alex", "Tereza", "Daniel"]
print(type(nomes3), nomes3)

nomes3 = tuple(nomes3)
print(type(nomes3), nomes3)


# Convertendo 'tupla' em 'lista'
nomes3 = list(nomes3)
print(type(nomes3), nomes3)