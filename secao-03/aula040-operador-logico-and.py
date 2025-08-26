"""
Operadores lógicos:
and (e), or (ou), not (não).
 
and - Todas as condições precisam ser verdadeiras.

Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.

Considerados falsy (considerado falso): 0, 0.0, ""(string vazia), False.

Também existe o tipo 'None' que é usado para representar um 'não valor'.
"""

# Primeiro exemplo de uso do "and":
entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")
senha_permitida = "123456"

if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print("Sair")

print("------------------")

# Segundo exemplo de uso do "and": Avaliação de curto circuito.
print(True and True)
print(True and True and True)
print(True and False and True)
print("------------------")


# Terceiro exemplo de uso do "and": Avaliação de curto circuito.
print(bool("")) # Retorna False
print(bool(" ")) # Retorna True
print(bool(0)) # Retorna False
print(bool(0.0)) # Retorna False
print(True and 0 and True) # Retorna 0
print("------------------")