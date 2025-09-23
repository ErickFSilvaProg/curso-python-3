"""
# Listas em Python: (São semelhantes aos 'arrays' em outras linguagens.)

    Tipo list - Mutável
    Suporta vários valores de qualquer tipo.

    Conhecimentos reutilizáveis - Índices e fatiamento.

    - Métodos úteis:

        del - Apaga um índice específico.
        insert - Adiciona um item no índice escolhico.
        
        append - Adiciona um item ao final da lista.
        pop - Remove um item do final da lista ou de um índice escolhido.
        
        clear - Limpa/esvazia a lista.
        extend - Estende a lista.
        + - Concatena listas.

"""

lista = [10, 20, 30, 40]
print(f"Lista inicial: {lista}")
print()


# revisando:

lista.append("Luiz") # Adiciona um item ao final da lista.
lista.append("Guilherme")
print(lista)

lista.pop() # Remove um item do final da lista ou de um índice escolhido.
print(lista)

del lista[-1] # Apaga um item específico.
print(lista)

lista.clear() # limpa/esvazia a lista.
print(lista)
print()


#        0   1   2   3
lista = [10, 20, 30, 40]
print(f"Lista inicial: {lista}")
print()

# Inserindo item em qualquer lugar da lista:
#       índice, valor
lista.insert(0, 5)
lista.insert(3, 300)
lista.insert(-1, "último?")
print(lista)

lista.insert(100, 100) # Ele irá inserir no último índice. Não existe o índice "100".
print(lista)
print()