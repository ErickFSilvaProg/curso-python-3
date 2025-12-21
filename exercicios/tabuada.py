# Tabuada de multiplicação:

operando = 1

while True:
    operando = 1
    tabuada = input("- Qual tabuada você quer?: ")
    print()

    if tabuada == "sair":
        break

    try:
        numero = int(tabuada)

        while operando <= 10:
            print(f"{numero} x {operando} = {numero * operando}")
            operando += 1
        
        print()
    except:
        print("Digite um número válido")
        print()