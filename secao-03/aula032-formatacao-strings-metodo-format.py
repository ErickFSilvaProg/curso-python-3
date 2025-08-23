"""
- str.format(): 

    Método que permitem inserir variáveis e expressões dentro de outras strings para criar uma saída controlada e mais legível.

    O método str.format() usa chaves {} como marcadores de posição que são preenchidos pelos argumentos passados ao método, enquanto as f-strings, mais modernas, incorporam expressões diretamente dentro de literais de string.
    
    Ambas são alternativas poderosas ao operador de formatação mais antigo (%) e permitem controle detalhado sobre a aparência, como o formato de números e alinhamento de texto.

    Tudo em python é um objeto.
    Tudo que vier após um parâmetro nomeado, precisa ser nomeado.
"""

a = "A"
b = 11
c = 1.1

# string = "a={} b={} c={:.2f} {}"
# - Geraria o erro: IndexError: Replacement index 3 out of range for positional args tuple

# Recuperando os valores sem índices:
string_1 = "a={} b={} c={}"
print(string_1.format(a, b, c))

# Recuperando valores com índices:
string_2 = "b={1} a={0} a={0} b={1} c={2:.2f}"
print(string_2.format(a, b, c))

string_3 = "{nome2} {nome1} {nome2} {nome3} {nome1} {nome3:.3f}"
print(string_3.format(nome1 = a, nome2 = b, nome3 = c))
print()