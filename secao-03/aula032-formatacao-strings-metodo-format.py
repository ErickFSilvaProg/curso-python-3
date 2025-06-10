a = 'A'
b = 'B' * 2
c = 1.1
string = 'a={} b={} c={nome3:.2f} d={nome4} e={nome5}'

# Tudo em python é um objeto.
# Tudo que vier após um parâmetro nomeado, precisa ser nomeado.

formato = string.format(
    a,
    b,
    nome3=c,
    nome4=a,
    nome5=b
    )

print(formato)