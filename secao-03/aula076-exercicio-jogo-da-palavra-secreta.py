# Exercício - Jogo da palavra secreta.

"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

1. Você irá propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.

2. Quando o usuário digitar uma letra, você irá conferir se a letra digitada está na palavra secreta.

    2.1. Se a letra digitada estiver na palavra secreta, exiba a letra.
    2.2. Se a letra digitada não estiver na palavra secreta, exiba '*'.

3. Faça a contagem de tentativas do seu usuário.
"""

# Bibliotecas:
import os


# Variáveis Globais:
palavra_secreta = "perfume"
letras_acertadas = ""
numero_tentativas = 0


while True:
    # Variáveis locais:
    palavra_formada = ""

    # Recebe a letra do usuário:
    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    # Garante que apenas um caractere seja digitado:
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    # Valida a letra digitada com a palavra secreta:
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    # Monta a paralavra secreta de acordo com as letras recebidas:
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    # Limpa a tela deixando apenas a palavra formada e a entrada do usuário:
    if palavra_formada != "":
        os.system("cls")
        print("Palavra formada:", palavra_formada)
    
    # Limpa a tela e exibe o resultado:
    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("Você ganhou, parabéns!")
        print(f"A palavra era {palavra_formada}.")
        print(f"Número de tentativas: {numero_tentativas}\n")
        break