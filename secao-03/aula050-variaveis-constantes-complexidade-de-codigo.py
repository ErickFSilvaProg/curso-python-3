"""
CONSTANTES: variáveis que não mudam de valor.

Obs.: Não há constantes em python.
      Mas há uma conversão da comunidade para declarar constantes.

Muitas condições no mesmo "if" torna-se mais complexo.

"""

velocidade = 61 # Velocidade atual do carro.
local_carro = 101 # Local em que o carro está na estrada.

RADAR_1 = 60 # Velocidade máxima do radar 1.
LOCAL_1 = 100 # Local onde o radar 1 está.
RADAR_RANGE = 1 # A distância onde o radar pega.

velocidade_carro_radar_1 = velocidade > RADAR_1
# A barra permite a quebra de liha no código.
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                        local_carro <= (LOCAL_1 + RADAR_RANGE)


if velocidade_carro_radar_1:
    print("Velocidade carro passou do radar 1")

    if carro_multado_radar_1:
        print("Carro multado em radar 1.")