"""
- Exercício:

1. Peça ao usuário para digitar seu nome;
2. Peça ao usuário para digitar sua idade;
3. Se o nome e a idade forem digitados, exiba:
    
    "Seu nome é [nome]"
    "Seu nome invertido é {nome invertido}"
    "Seu nome contém (ou não) espaços"
    "Seu nome tem [n] letras"
    "A primeira letra do seu nome é [letra]"
    "A última letra do seu nome é [letra]"

4. Se nada for digitado no nome ou idade, exiba:

    "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
espaco = "não contém"
print()

if nome and idade:

    if " " in nome:
        espaco = "contém"

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome {espaco} espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")

print()