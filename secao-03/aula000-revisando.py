# Exercício - Jogo da palavra secreta.

"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

1. Você irá propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.

2. Quando o usuário digitar uma letra, você irá conferir se a letra digitada está na palavra secreta.

    2.1. Se a letra digitada estiver na palavra secreta, exiba a letra.
    2.2. Se a letra digitada não estiver na palavra secreta, exiba '*'.

3. Faça a contagem de tentativas do seu usuário.
"""


import os
# *****************************************

palavra_secreta = "Programação"
numero_tentativas = 0

# Servem como base de dados para consultas:
letras_acertadas = ""
letras_erradas = ""
# *****************************************


while True:
    letra_digitada = input("Digite uma letra ou $ para sair: ")

    if letra_digitada != "$":
        numero_tentativas += 1

        if len(letra_digitada) > 1:
            os.system("cls") # Limpa o terminal
            
            print("(Digite apenas uma letra.)\n")
            continue