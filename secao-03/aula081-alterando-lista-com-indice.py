"""
- Listas em Python: (São semelhantes aos 'arrays' em outras linguagens.)

Tipo list - Mutável
Suporta vários valores de qualquer tipo.

Conhecimentos reutilizáveis - Índices e fatiamento.

Métodos úteis: 
    append - Adiciona um item ao final da lista. 
    insert - Adiciona um item no índice escolhico.
    pop - Remove do final ou do índice escolhido.
    del - Apaga um índice.
    clear - Limpa a lista.
    extend - Estende a lista.
    + - Concatena listas.
"""


lista = [10, 20, 30, 40]
print("Lista completa:", lista)
print(lista[2])

numero = lista[2]
print(numero)

lista[2] = 300
print(lista[2])
print(f"Lista completa: {lista}")

# Deletando item da lista:
del lista[0]
print(f"Lista completa: {lista}")

# Adicionar item ao final da lista:
lista.append(50)
lista.append(60)
lista.append(70)
lista.append(80)
print(f"Lista completa: {lista}")

#  Remove item do final da lista:
lista.pop()
print(f"Lista completa: {lista}")

# Exemplos:
ultimo_valor = lista.pop()
print(f"Lista completa: {lista}. (Removido, {ultimo_valor})")