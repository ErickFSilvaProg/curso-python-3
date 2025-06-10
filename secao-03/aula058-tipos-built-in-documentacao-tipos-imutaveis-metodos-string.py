# https://docs.python.org/pt-br/3.13/contents.html

# Tipos com valores imutáveis: str, int, float, bool.


string = "luiz Otávio"
# string[3] = "ABC"
print(string[3])

outra_variavel = f"{string[:3]}ABC{string[4:]}"
print(outra_variavel)

print(string.capitalize())
print(string.zfill(20))