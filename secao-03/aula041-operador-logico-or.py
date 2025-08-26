"""
Operadores lógicos:
and (e), or (ou) e not (não).

or (ou) - Qualquer condição verdadeira avalia toda a expressão como verdadeira.

Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.

São considerados falsy (considerado falso): 0, 0.0, '', False.

Também existe o tipo 'None' que é usado para repersentar um 'não valor'.
"""

# Primeiro exemplo de uso do "and":
entrada = input("[E]ntrar [S]air: ")
senha_permitida = "123456"
sair_str = "Sair"

if entrada == "E" or entrada == "e":
    senha_digitada = input("Senha: ")

    if senha_digitada == senha_permitida:
        print("Entrou")
    else:
        print(f"{sair_str}")

else:
     print(f"{sair_str}")
print()

# Segundo exemplo de uso do "and": Avaliação de curto circuito.
print(True or False) # Retorna True
print(True or False or 0) # Retorna True
print(0 or False or 0 or 'abc') # Retorna "abc"
print(0 or False or 0 or 'abc' or True) # Retorna "abc"
print()

# Terceiro exemplo de uso do "and": Avaliação de curto circuito.
senha = input("Senha: ") or "Sem senha"
print(senha)
print()