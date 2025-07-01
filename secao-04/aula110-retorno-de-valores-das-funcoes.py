"""
Retorno de valor das funções (return):

'print()' é uma função que 'exibe' valor na tela, mas não 'retorna' valor algum.
'None' em Python significa 'não valor'.
O 'return' faz com que a funções retorne apenas um valor, podendo ser uma 'lista' ou uma 'tupla'.
O 'print()' e o 'return' são 'coisas' diferentes em Python.
Após o 'return' o Python não executa mais nada.

Existem dois tipos de funções:
    1º Funções que apenas executam ações.
        Ex.: print()

    2º Funções que retornam valores.
        Ex: def soma(x, y):
                return x + y
"""

# Exemplo com o print():
variavel = print('Erick')
print(variavel)
print(variavel is None)
print()

variavel = None
print(variavel)
print(variavel is None)
print()


# Exemplo de função que retorna valor:
def soma(x, y):
    if x > 10:
        return x, 10
    elif y > 10:
        return [10, y]
    
    return x + y

soma1 = soma(1, 1)
print(soma1)

soma2 = soma(2, 2)
print(soma2)

soma11 = soma(11, 10)
print(soma11)

soma12 = soma(10, 12)
print(soma12)

soma3 = soma(3, 3)
print(soma3)