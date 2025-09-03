"""
https://docs.python.org/pt-br/3.13/contents.html

- Tipos com valores imutáveis:

    str, int, float, bool.

"""

string = "Erick Ferreira"

print(string)
print(string[4])

try:
    # Retornaria o erro: IndentationError: unexpected indent
    string[4] = "i"
except:
    print(string[4])
print()

outra_variavel = f"{string[:3]}ck{string[5:]}"
print(outra_variavel)
print()

# Coloca o primeiro caractere da string maiúsculo.
print(string.capitalize())

# Complementa a string co zeros até completar a quantidade informada.
print(string.zfill(20))
print()