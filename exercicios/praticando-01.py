# Praticando 01:

lista_pessoas = []
fim_prog = False

while fim_prog is False:
    def funcionario():
            cad_pessoas = input("Cadastro de pessoas. [$]air: ")
            
            if cad_pessoas == "$":
                return True
            
            lista_pessoas.append(cad_pessoas)
            funcionario()

    fim_prog = funcionario()

print("\nPrograma encerrado...")
print(lista_pessoas)