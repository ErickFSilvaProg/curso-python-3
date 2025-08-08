"""
# Tipo: bool (boolean).
    - Ao questionar algo em um programa, só existem duas respostas possíveis: True (sim) ou False (não).
    - Existem vários operadores para 'questionar', dentre eles, o operador lógico '==' (igual) que compara se um valor é igual a outro.
"""

# bool:
print(type(10 == 10), 10 == 10)
print(type(10 == 11), 10 == 11)
print()

print(type("oi" == "oi"), "oi" == "oi")
print(type('oi' == 'ei'), 'oi' == 'ei')
print()

print(type(10) == type(11))
print(type('casa') == type("uva"))