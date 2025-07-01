"""
args - Argumentos não nomeados.
* - *args (empacotamento e desempacotamento)
"""

# Lembre-se do desempacotamento:
x, y, *resto = 1, 2, 3, 4, 5, 6
print(x, y, resto)
print()


# Empacotamento de argumentos não nomeados:
def soma(*args):
    total = 0

    for numero in args:
        total += numero
    
    print(total)

soma(1, 2, 3, 4, 5, 6)
print()


def soma2(*args):
    total = 0

    for numero in args:
        total += numero
    
    return total

print(soma2(10,20,30,40,50,60))
print()


# Função soma:
print(sum((1, 2, 3, 4, 5, 6)))