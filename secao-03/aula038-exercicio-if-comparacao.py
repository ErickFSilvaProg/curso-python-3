# Exercício de programação com 'if' e 'comparação':

valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
print()

primeiro_valor = int(valor1)
segundo_valor = int(valor2)

# if primeiro_valor > segundo_valor:
#     print(f"{primeiro_valor=} é maior do que {segundo_valor=}")
#     print()
# elif segundo_valor > primeiro_valor:
#     print(f"{segundo_valor=} é maior do que {primeiro_valor=}")
#     print()
# else:
#     print("Os valores são iguais.")
#     print()


if primeiro_valor == segundo_valor:
    print("Os valores são iguais.")
    print()
else:
    if primeiro_valor > segundo_valor:
        print(f"{primeiro_valor=} é maior do que {segundo_valor=}")
        print()
    else:
        print(f"{segundo_valor=} é maior do que {primeiro_valor=}")
        print()