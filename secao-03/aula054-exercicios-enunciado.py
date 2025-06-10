# 1. Faça um programa que peça ao usuário para digitar um número inteiro e informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

try:
    numero_digitado = int(input("Digite um número inteiro: "))
    
    if numero_digitado % 2 == 0:
        print(f"O número {numero_digitado} é par.")
    else:
        print(f"O número {numero_digitado} é impar.")

except:
    print("Você não digitou um número inteiro.")


# 2. Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.

print()
horaDigitada = input("Informe a hora: ")
horaErrada = "Essa hora não existe..."

try:
    hora = int(horaDigitada)

    if hora >= 0 and hora <= 11:
        print("Bom dia!")

    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")

    elif hora >= 18 and hora <= 23:
        print("boa noite!")
    
    else:
        print(horaErrada)

except:
    print(horaErrada)


# 3. Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva: "Seu nome é curto". Se estiver entre 5 e 6 letras, escreva: "Seu nome é normal". Mas, se for maior que 6 letras, escreva: "Seu nome é muito grande".

print()
primeiroNome = input("Digite seu 1º Nome: ")
tamanho_nome = len(primeiroNome)

if tamanho_nome <= 4:
    print("Seu nome tem o tamanho curto.")

elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print("Seu nome tem o tamanho normal.")

else:
    print("Seu nome tem o tamanho muito grande.")