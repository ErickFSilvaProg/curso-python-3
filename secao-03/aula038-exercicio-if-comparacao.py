# Exercício

primeiro_valor = int(input('Digite o Primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print(f'"primeiro_valor({primeiro_valor})" é maior do que "segundo_valor({segundo_valor})"')

elif primeiro_valor == segundo_valor or segundo_valor == primeiro_valor:
    print(f'"primeiro_valor({primeiro_valor})" é igual ao "segundo_valor({segundo_valor})"')

else:
    print(f'"segundo_valor({segundo_valor})" é maior do que "primeiro_valor({primeiro_valor})"')