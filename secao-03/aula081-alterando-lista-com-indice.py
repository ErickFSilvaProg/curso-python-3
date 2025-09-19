"""
# Listas em Python: (São semelhantes aos 'arrays' em outras linguagens.)

    Tipo list - Mutável
    Suporta vários valores de qualquer tipo.

    Conhecimentos reutilizáveis - Índices e fatiamento.

    - Métodos úteis:

        del - Apaga um índice.
        insert - Adiciona um item no índice escolhico.
        
        append - Adiciona um item ao final da lista.
        pop - Remove do final ou do índice escolhido.
        
        clear - Limpa a lista.
        extend - Estende a lista.
        + - Concatena listas.

"""


# Lista:
lista = [10, 20, 30, 40]
print(f"Lista original:")
print(lista)
print()

print(f"Índice 2 alterado:")
lista[2] = 300
print(lista)
print()


# Deletando índices da lista: Informe o índice.
print(f"Deletado o índice 2: {lista[2]}")
del lista[2]
print(lista)
print()


# Adicionar itens ao final da lista:
print(f"Adicionado índices: 50, 60, 70")
lista.append(50)
lista.append(60)
lista.append(70)
print(lista)
print()


# Remove item do final da lista:
print(f"Removido o último valor: {lista.pop()}")
print(lista)
print()