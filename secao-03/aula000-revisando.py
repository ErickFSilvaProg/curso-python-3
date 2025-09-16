"""
# Calculadora com while:

    - Algumas funções para string:

        startswith("[string]"): começa com...
        endswith("[string]"): termina com...

"""


while True:
    sair = input("Quer sair? [s]im: ").lower().startswith("s")
    
    if sair is True:
        break