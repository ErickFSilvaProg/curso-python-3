# Operadores lógicos:
# and (e), or (ou) e not (não).

# not (não) - Usado para inverter a expressão booleana.
# not True = False.
# not False = True.


senha = input('Senha: ')

if not senha:
    print('Digite a senha.')

elif senha != '123456':
    print('Senha incorreta.')

else:
    print('Logado.')


# Avaliação de curto circuito
print(True, not True)
print(False, not False)