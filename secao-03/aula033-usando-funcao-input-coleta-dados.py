"""
- input: Entreda de dados via terminal. 

    Função que interage com o usuário via terminal.
    Ele retorna um string para o programa.

"""

usuario = input("Qual o seu nome? ")

print(f"{usuario=}")
print(f"O seu nome é {usuario}")
print()


numero1 = input("Digite um número: ")
numero2 = input("Digite outro número: ")

int_numero1 = int(numero1)
int_numero2 = int(numero2)

print(f"A soma dos números é: {int_numero1 + int_numero2}")
print()