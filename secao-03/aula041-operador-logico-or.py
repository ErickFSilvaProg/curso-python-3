# Operadores lógicos:
# and (e), or (ou) e not (não).

# or (ou) - Qualquer condição verdadeira avalia toda a expressão como verdadeira.

# Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.
# São considerados falsy (considerado falso): 0, 0.0, '', False.
# Também existe o tipo 'None' que é usado para repersentar um 'não valor'.


entrada = input('[E]ntrar [S]air: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and entrada != '':
    senha_digitada = input('Senha: ')

    if senha_digitada == senha_permitida:
        print('Entrar')

else:
    print('Sair')


# Avaliação de curto circuito
print(True or False)
print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)