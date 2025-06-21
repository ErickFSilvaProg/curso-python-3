"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de 'inserir', 'apagar' e 'listar' valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""

import os

# ******************************************
mensagem_opcao = "Selecione uma opção"
opcao_entrada = ""
lista_compras = []

# ******************************************
try:
    
    # ******************************************
    while opcao_entrada != "s":

        print(f"\n{mensagem_opcao}")
        opcao_entrada = input("[i]nserir [a]pagar [l]istar [s]air: ")
        print()

        # INSERIR ########################################
        if opcao_entrada == "i":

            # ******************************************
            os.system("cls") # Limpa o terminal
            digitar_item = ""

            # ******************************************
            while digitar_item != "$":
                
                os.system("cls") # Limpa o terminal
                
                # ******************************************
                print(" - Item(ns) da lista:\n")
                
                if lista_compras != []:

                    for indice, item in enumerate(lista_compras):
                        print(f"{indice}) {item}")
                
                else:
                    print("\nNada para listar.")
                
                # ******************************************
                print("\n\n - Adicionar item à lista?\n")
                digitar_item = input("Digite o item | [$]air: ")
                
                if digitar_item == "":
                    continue

                if digitar_item != '$':
                    lista_compras.append(digitar_item)

                os.system("cls") # Limpa o terminal

        # APAGAR ########################################
        if opcao_entrada == "a":

            # ******************************************
            os.system("cls") # Limpa o terminal
            apagar_item = ""

            # ******************************************
            while apagar_item != "$":
                
                os.system("cls") # Limpa o terminal
                
                # ******************************************
                print(" - Item(ns) da lista:\n")
                
                if lista_compras != []:

                    for indice, item in enumerate(lista_compras):
                        print(f"{indice}) {item}")
                else:
                    print("\nNada para listar.")
                
                # ******************************************
                try:
                    print("\n\n - Apagar item da lista?\n")
                    apagar_item = input("Digite o item | [$]air: ")
                    
                    if apagar_item == "":
                        continue
                    elif apagar_item != '$':
                        
                        if lista_compras != []:
                            del lista_compras[int(apagar_item)]
                    
                    os.system("cls") # Limpa o terminal
                            
                except ValueError:
                    print("Por favor digite um número inteiro.")
                except IndexError:
                    print("Índice não existente na lista.")
                except:
                    print("Erro desconhecido na exclusão.")

        # LISTAR ########################################
        if opcao_entrada == "l":

            os.system("cls") # Limpa o terminal

            # ******************************************
            if lista_compras != []:

                os.system("cls") # Limpa o terminal
                print(" - Item(ns) da lista:\n")

                # ******************************************
                for indice, item in enumerate(lista_compras):
                    print(f"{indice}) {item}")

                print()
            else:
                os.system("cls") # Limpa o terminal
                print("\nNada para listar.")
        
        # ENTRADA VAZIA ########################################
        if opcao_entrada == "":
            
            os.system("cls") # Limpa o terminal
    
    # ******************************************
    os.system("cls") # Limpa o terminal
    print(
    """
    Programa finalizado!
    """)

# ******************************************
except:
    os.system("cls") # Limpa o terminal
    print(
    """
    Erro desconhecido. Programa finalizado!
    """)