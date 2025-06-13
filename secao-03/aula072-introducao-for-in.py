# Introdução ao 'for/in' - Estrutura de reperição para coisas finitas.

"""
# Exemplo de laço com interação finita:
texto = "Python"
i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])
    
    i += 1


# Exemplo de laço com interação infinita:
senha_salva = "123456"
senha_digitada = ""
repeticoes_erradas = 0
cont = 1
msg_logado = "Sistema logado.\n"

while senha_salva != senha_digitada:
    senha_digitada = input(f"Sua senha ({cont}ªx): ")
    
    if senha_digitada != senha_salva:
        repeticoes_erradas += 1
    
    cont += 1


print()
if repeticoes_erradas > 0:
    print(f"Você errou a senha {repeticoes_erradas} vezes.")
    print(msg_logado)

else:
    print(msg_logado)
"""


texto = "Python"
novo_texto = ""

for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)

print(novo_texto + "*")