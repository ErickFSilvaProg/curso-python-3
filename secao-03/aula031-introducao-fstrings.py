"""
- f-string: formatted string literal.

    Uma forma de formatar strings que permite incorporar expressões e variáveis dentro delas de maneira simples e legível, prefixando a string com a letra 'f' e usando {} para delimitar as expressões a serem avaliadas em tempo de execução.
    
    Introduzidas na versão 3.6, as f-strings são a maneira preferida de formatar strings em Python, tornando o código mais conciso e eficiente em comparação com métodos anteriores. 
"""

nome = "Erick"
altura = 1.75
peso = 82
imc = peso / (altura * altura)

string1 = f"{nome} tem {altura} de altura."
string2 = f"{nome} pesa {peso}kg."
string3 = F"{nome} tem um IMC de {imc:.2f}." # Formatando para duas casas decimais.

print(string1)
print(string2)
print(string3)