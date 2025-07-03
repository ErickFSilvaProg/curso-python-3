# Praticando 01:

lista_pessoas = []
cad_pessoas = ""

while cad_pessoas != "$":
    cad_pessoas = input("Cadastro de pessoas. [$]air: ")

    if cad_pessoas != "$":
        lista_pessoas.append(cad_pessoas)
        print(lista_pessoas)

print(lista_pessoas)