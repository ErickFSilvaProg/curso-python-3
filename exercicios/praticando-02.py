# Praticando 02:

# Importa a bibioteca do sistema:
import os

# Variáveis, Listas, Dicionários:
lista_funcionarios = []

# Função:
def funcionario():
    
    # Laço para cadastrar funcionários:
    while True:
        os.system('cls') # Limpa o terminal
        print('# Cadastro de funcionário:\n')

        # Coleta os dados do funcionário:
        nome = input('Nome: ')
        profissao = input('Profissão: ')
        salario = input('Salário: ')
        novo_cad = input('\nCadastrar funcionário? [S]im | [N]ão: ')

        # Adiciona os dados coletados em um dicionário:
        pessoa = {
                'Nome': nome,
                'Profissao': profissao,
                'Salario': salario
        }

        # Armazena os dados do dicionário em uma lista de funcionários:
        lista_funcionarios.append(pessoa)
    
        # Condicional para finalizar o programa:
        if novo_cad == 'N' or novo_cad == 'n':
                return True

# Chamada da função:
funcionario()

# Programa encerrado:
os.system('cls') # Limpa o terminal
print('# Programa encerrado...\n')

# Imprime os dados cadastrados:
for indice, dados in enumerate(lista_funcionarios):
	print(indice)

	for dado in dados:
		print(f'{dado}: {dados[dado]}')
	
	print()