"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de 'inserir', 'apagar' e 'listar' valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

# Solução do professor Luiz.

# Imports
import os

# Variáveis
lista = []

# Laço para automatizar o programa:
while True:
    print('\nSelecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    # Opção I:
    if opcao == 'i':
        os.system('cls')
        
        valor = input('Valor: ')
        lista.append(valor)
    
    # Opção A:
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        
        # Tratando os erros:
        try:
            indice = int(indice_str)
            del lista[indice]
        
        except ValueError: # Erro no tipode valor digitado/convertido.
            print('Por favor digite um número inteiro.')
        
        except IndexError: # Erro na posição informada do item.
            print('Índece não existe na lista.')
        
        except Exception: # Erros gerais.
            print('Erro desconhecido.')
    
    # Opção L:
    elif opcao == 'l':
        os.system('cls')
        
        # ---------------------------
        if len(lista) == 0:
            print('Nada para listar')

        # ---------------------------
        for i, valor in enumerate(lista):
            print(i, valor)
    
    # Escolha uma opção válida:
    else:
        print('Por favor, escolha "i", "a", "l".')