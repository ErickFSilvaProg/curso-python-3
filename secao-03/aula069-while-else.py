"""
- while/else

    Quando o "laço while" é executado completamente, sem que haja uma saída forçada do mesmo, o "else" é executado.
    Do contrário, o 'else' não será executado.

"""

# string = "Python com Django"
string = "Python"
i = 0

while i < len(string):
    letra = string[i]

    if letra == " ":
        print()
        print("Encontrei um espaço na string")
        break
    
    print(letra)
    i += 1
else:
    print()
    print("Não encontrei um espaço na string")

print()
print("Fora do 'while'.")
print()