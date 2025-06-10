"""
- Exercício:

1. Peça ao usuário para digitar seu nome;
2. Peça ao usuário para digitar sua idade;
3. Se o nome ou idade forem digitados, exiba:
    
    "Seu nome é [nome]"
    "Seu nome invertido é {nome invertido}"
    "Seu [nome] contém (não) espaços"
    "Seu nome tem [n] letras"
    "A primeira letra do seu nome é [letra]"
    "A última letra do seu nome é [letra]"

4. Se nada for digitado no nome ou idade, exiba:

    "Desculpe, você deixou campos vazios."
"""


nomeUsuario = input('Digite seu nome: ')
idadeUsuario = input('Digite sua idade: ')

if nomeUsuario and idadeUsuario:
    print(f'Seu nome é {nomeUsuario}.')
    print(f'Seu nome invertido é {nomeUsuario[::-1]}.')

    if ' ' in nomeUsuario:
        print(f'Seu nome contém espaço.')
    else:
        print(f'Seu nome não contém espaço.')

    print(f'Seu nome tem {len(nomeUsuario)} letras')
    print(f'A primeira letra do seu nome é {nomeUsuario[0]}.')
    print(f'A última letra do seu nome é {nomeUsuario[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')

