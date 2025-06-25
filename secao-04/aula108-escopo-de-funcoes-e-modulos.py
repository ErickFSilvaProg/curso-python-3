"""
Escopo de função em Python.
Escopo é o local que aquele código pode atingir.
Existe o escopo global e o local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

x = 1

def escopo_1():
    
    x = 10
    print(f"Valor do 'escopo_1': {x}")

    def escopo_2():

        x = 100
        print(f"Valor do 'escopo_2': {x}")

    escopo_2()

escopo_1()
print(f"Valor do 'escopo global' de 'x': {x}")