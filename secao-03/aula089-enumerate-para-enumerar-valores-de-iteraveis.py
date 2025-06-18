# enumerate - Enumera iteráveis (índices)

pessoas = ["Maria", "Helena", "Luiz"]
print(pessoas)

pessoas.append("João")
print(pessoas)
print()

# Esta classe retornará um objeto, um 'iterator'.
# Após o 'iterator' ser consumido ele elimina os valores contidos nele.
pessoas_enumeradas = enumerate(pessoas)
print(type(pessoas_enumeradas))
print(next(pessoas_enumeradas))
print()

for item in pessoas_enumeradas:
    print(item)
print()

# Para evitar isso, chame a classe direto no 'for':
for pessoa in enumerate(pessoas):
    print(pessoa)
print()

for pessoa in enumerate(pessoas):
    indice, nome = pessoa
    print(indice, nome)
print()

for indice, nome in enumerate(pessoas):
    print(indice, nome)
print()

# Conversão de tipos com o 'enumerate'. 'Lista' e 'tupla':
lista_nomes = list(enumerate(pessoas))
print(lista_nomes)

lista_nomes = list(enumerate(pessoas, start=10))
print(lista_nomes)

print()
lista_nomes = tuple(enumerate(pessoas))
print(lista_nomes)

lista_nomes = tuple(enumerate(pessoas, start=100))
print(lista_nomes)
print()