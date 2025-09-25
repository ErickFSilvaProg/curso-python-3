"""
- Cuidados com dados mutáveis:

    O sinal de atribuição [=], em dados imutáveis, copia o valor.
    O sinal de atribuição [=], em dados mutáveis, aponta para o mesmo valor na memória.

# Listas em Python: (São semelhantes aos 'arrays' em outras linguagens.)

    - Tipo list - Mutável

        Suporta vários valores de qualquer tipo.
        Conhecimentos reutilizáveis - Índices e fatiamento.

    - Métodos úteis:

        append - Adiciona um item ao final da lista. 
        insert - Adiciona um item no índice escolhico.
        pop - Remove do final ou do índice escolhido.
        del - Apaga um índice.
        clear - Limpa a lista.
        extend - Estende a lista.
        + - Concatena listas.
    
"""

# Exemplo de dados imutáveis: O sinal de atribuição [=], em dados imutáveis, copia o valor.
nome = "Luiz"
outro_nome = nome
nome = "Erick"

print(nome)
print(outro_nome)
print()


# Exemplo de dados mutáveis: O sinal de atribuição [=], em dados mutáveis, aponta para o mesmo valor na memória.
lista_a = ["Luiz", "Maria"]
print(lista_a)

lista_b = lista_a
print(lista_b)
print()

lista_c = lista_a.copy() # Utilizando o método copy() os valores são copiados e não mais referenciados.
print(lista_c)
print()

lista_a[0] = "Pedro"
print(lista_a)
print(lista_b)
print(lista_c)
print()