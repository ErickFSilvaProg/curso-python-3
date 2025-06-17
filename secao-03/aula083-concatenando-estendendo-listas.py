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

# 
lista_a = [1,2,3]
lista_b = [4,5,6]

# Concatenando as listas:
lista_c = lista_a + lista_b

# O método 'extend' não retorna nada, apenas executa uma ação:
lista_a.extend(lista_b)

# 
print(lista_c)
print(lista_a)