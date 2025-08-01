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

Cuidados com dados mutáveis:
    = - Copiado o valor (imutaveis)
    = - Aponta para o mesmo valor na memória (mutável)
"""

# 
lista_a = ["Luiz", "Maria", 1, True, 1.2]
print(f"Lista A: {lista_a}")

lista_b = lista_a.copy()
print(f"Lista B: {lista_b}")

lista_a[0] = "Qualquer coisa"
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
