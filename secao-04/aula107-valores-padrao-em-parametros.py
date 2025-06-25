"""
Valores padrão para parâmetros.
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

Refatorar: editar (melhorar) o código.
"""

# Zero é considerado 'falsi'
# Obs.: Após o primeiro parâmetro receber um valor padrão, todos os outros deverão receber valor padrão também.
def soma(x, y=None, z=None):

    if z is not None:
        print(f"{x=} + {y=} + {z=} = {x+y+z}")
    else:
        print(f"{x=} {y=} = {x+y}")

soma(100, 200)
soma(7, 9, 0)
soma(5, 1)