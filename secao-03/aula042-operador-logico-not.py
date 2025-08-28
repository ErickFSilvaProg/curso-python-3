"""
Operadores lógicos:
    
    and(e), or(ou), not(não).

not - Usado para inverter a expressão booleana:
    
    not True = False
    not False = True

"""

# Exemplo:
senha = input("Senha: ")

if not senha:
    print("Digite a senha")
elif senha != "123456":
    print("Senha incorreta")
else:
    print("Logado")

print()


# Avaliação de curto ciruito:
print(True, not True)
print(False, not False)
print()
