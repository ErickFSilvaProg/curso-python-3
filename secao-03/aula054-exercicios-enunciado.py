"""
    1. Faça um programa que peça ao usuário para digitar um número inteiro e informe se este número é par ou ímpar.
    Caso o usuário não digite um número inteiro, informe que não é um número inteiro:

"""

numero = input("Digite um número inteiro: ")

try:
    numero_inteiro = int(numero)

    if numero_inteiro % 2 == 0:
        print(f"O número {numero_inteiro} é par.\n")
    else:
        print(f"O número {numero_inteiro} é impar.\n")
except:
    print(f"'{numero}' não é um número inteiro.\n")


"""
    2. Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
    Ex.: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23:

"""

hora = input("Informe que horas são: ")

try:
    hora_atual = int(hora)

    if hora_atual >= 0 and hora_atual <= 11:
        print("Bom dia!\n")
    elif hora_atual >= 12 and hora_atual <= 17:
        print("Boa tarde!\n")
    elif hora_atual >= 18 and hora_atual <= 23:
        print("Boa noite!\n")
    else:
        print("A hora informada não existe!\n")
except:
    print("Por favor, digite apenas números inteiros.\n")


"""
    3. Faça um programa que peça o primeiro nome do usuário.
    Se o nome tiver 4 letras ou menos, escreva: "Seu nome é curto".
    Se estiver entre 5 e 6 letras, escreva: "Seu nome é normal".
    Mas, se for maior que 6 letras, escreva: "Seu nome é muito grande":
"""

nome = input("Informe seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto.\n")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é normal.\n")
    else:
        print("Seu nome é muito grande.\n")
else:
    print("Digite mais de uma letra.\n")