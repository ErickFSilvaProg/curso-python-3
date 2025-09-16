"""
- Algumas funções para string:

    startswith("[string]"): começa com...
    endswith("[string]"): termina com...

"""


# Variáveis globais:
numeros_validos = ... # Flag para validar números digitados.
texto_resultado = "\nResultado da operação: "
operadores_permitidos = "+-*/"


# Calculadora com while:
while True:
    # - Tratando possíveis erros da entrada dos dados:
    try:
        # - Entrada de dados:
        numero_1 = float(input("Digite um número: "))
        numero_2 = float(input("Digite outro número: "))
        operador = input("Digite o operador (+-*/): ")
        numeros_validos = True
    except:
        numeros_validos = None
	

    # - Reinicia o programa caso retorne algum erro:
    if numeros_validos is None:
        print("(O número digitado é inválido.)\n")
        continue # Retornará ao início do programa em caso de erro.
    
    if operador not in operadores_permitidos:
        print("(O operador digitado é inválido.)\n")
        continue # Retornará ao início do programa em caso de erro.
    
    if len(operador) > 1:
        print("(Digite apenas um operador.)\n")
        continue # Retornará ao início do programa em caso de erro.


    # - Realizando as operações:
    if operador == "+":
        print(texto_resultado, numero_1 + numero_2)
    elif operador == "-":
        print(texto_resultado, numero_1 - numero_2)
    elif operador == "*":
        print(texto_resultado, numero_1 * numero_2)
    elif operador == "/":
        print(texto_resultado, numero_1 / numero_2)
    else:
        print("Nunca deveria chegar aqui.")


    # - Opção para sair do programa:
    # 'lower()': converte a string em minúscula.
    # 'startswith("[string]"): função que retorna um 'bool'.
    sair = input("\nQuer sair? [s]im: ").lower().startswith("s") 

    if sair is True:
        break
    else:
        print()

print("\nAcabou...")