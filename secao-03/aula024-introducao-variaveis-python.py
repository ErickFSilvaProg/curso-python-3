"""
Variáveis são usadas para salvar algo na memória do computador.

PEP8 - Guia de estilo para o código Python.
    
    https://pep8.org/

    Sempre inicie variáveis com letras minúsculas.
    
    Podemos utilizar números ou underline para compor o nome da variável.

    O sinal de '=' é o operador de atribuição. Ele é usado para atribuir um valor a um nome (uma variável).

    Padrão Snake case:
    Ex.: nome_variavel = expressao

"""

nome_completo = "Erick Ferreira da Silva"
print(nome_completo)

soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)

int_1 = int("1")
print(type(int_1), int_1)
print(type(bool(int_1)), bool(int_1))

nome = "Erick"
idade = 38
maior_idade = idade >= 18
print("Nome:", nome, "Idade:", idade)
print("É maior?", maior_idade)
print()