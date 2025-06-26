"""
Retorno de valor das funções (return):

'None' em Python significa 'não valor'.
'print()' é uma função que exibe valor.

Existem dois tipos de funções:
    1º Funções que apenas executam ações.
        Ex.: print()

    2º Funções que retornam valores.
        Ex: def soma(x, y):
                return x + y
"""

def soma(x, y):

    if x > 10:
        return [10, 20] # Retornará uma 'tupla'.
    
    return x + y # Nada será executado após o 'return'.

soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(soma1)
print(soma2)
print(soma1 + soma2)
print(soma(11,55))