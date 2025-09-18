"""
Aula 30 - Constantes
Constante = Constantes são variáveis cujo valor não deve ser alterado durante a execução do programa.
Constantes são úteis para armazenar valores que não devem ser modificados, como configurações, limites ou valores fixos.
Muitas condições no mesmo if (ruim)
<-Contagem de complexidade (muito ruim)
"""
velocidade = 61  #velocidade atual do carro
local_carro = 100 #local atual do carro

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local do radar 1
RADAR_RANGE = 1 #raio de alcance do radar 1

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
      local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('velocidade do carro que passou pelo radar 1:')

    if carro_passou_radar_1:
        print('Carro passou pelo radar 1!')

if carro_passou_radar_1 and vel_carro_passou_radar_1:    
    print('Carro multado em radar 1!')