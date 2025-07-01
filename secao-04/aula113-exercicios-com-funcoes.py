"""
- Exercícios com funções:

1. Crie uma função que multiplica todos os argumentos não nomeados recebidos. Retorne o valor para uma variável e mostre o valor da variável.
2. Crie uma função que fale se o número é par ou ímpar. Retorne se o número é par ou ímpar.
"""

# Esercício 1:
def multiplicacao(*args):
    total = 1

    for numero in args:
        total *= numero
    
    return total

print(multiplicacao(1, 2, 3, 4))


# Exercício 2:
def parImpar(num):
    multiplo_de_dois = num % 2 == 0

    if multiplo_de_dois:
        return f"O número {num} é par."
    
    return f"O número {num} é ímpar."

print(parImpar(20))
print(parImpar(23))
print(parImpar(0))