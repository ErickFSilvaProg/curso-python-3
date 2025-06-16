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

CRUD: 
    create - 
    read - 
    update - 
    delete - 
"""


lista = [10, 20, 30, 40]
print(lista)

lista.append("Luiz")
print(lista)

nome = lista.pop()
print(nome)

lista.append(1233)
print(lista)

del lista[-1]
print(lista)

lista.clear()
print(lista)

lista.insert(0, 0)
lista.insert(1, 10)
lista.insert(2, 20)
lista.insert(3, 30)
lista.insert(4, 40)
print(lista)

lista.insert(1, 1)
lista.insert(100, 100) # Ele irá inserir no último índice, já que não existe o índice '100'.
print(lista)