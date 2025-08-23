"""
'...' refere-se ao objeto Ellipsis.

Usado para indicar código que está incompleto ou pendente, como em funções e classes que ainda serão implementadas.

Elas também têm usos mais técnicos, como espaço reservado para tipos em dicas de tipo (type hints) e em fatiamento (slicing) para indicar "tudo" nas dimensões não especificadas, especialmente com bibliotecas como o NumPy. 

"""

nome = "Erick"
altura = 1.75
peso = 82
imc = ...

imc = peso / (altura * altura)

print(
    nome, "tem", altura, "de altura, pesa", peso, "quilos e seu IMC é", imc
)