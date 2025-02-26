# CONSTANTE: são "variáveis" que não vão mudar, ou seja, não é possível reatribuir outros valores à ela dentro do código

# A legibilidade do código não foi levada em extrema consideração, está apenas para fins didáticos

#função apenas para criar uma linha no terminal e dividir os exemplos para melhor visualização
def linha():
    print()
    print('-'*50)
    print()

# Variáveis mutáveis
velocidade1 = 61 # velocidade atual do carro, pode mudar a qualquer momento
localCarro1 = 90 # posição do carro na rodovia, o que também pode mudar a qualquer momento

# Constantes imutáveis
RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está na rodovia
RADAR_RANGE1 = 1 # a distância onde o radar pega

if velocidade1 > RADAR_1:
    print('A velocidade do carro excedeu o limite do Radar 01.')

if localCarro1 >= (LOCAL_1 - RADAR_RANGE1) and localCarro1 <= (LOCAL_1 + RADAR_RANGE1) and velocidade1 > RADAR_1:
    print('Você tomou uma multa pelo Radar 01.')

linha()
# Exemplo 2
 
velocidade2 = 69 # velocidade atual do carro, pode mudar a qualquer momento
localCarro2 = 99 # posição do carro na rodovia, o que também pode mudar a qualquer momento

# Constantes imutáveis
RADAR_2 = 60 # Velocidade máxima do radar 1
LOCAL_2 = 100 # local onde o radar 1 está na rodovia
RADAR_RANGE2 = 1 # a distância onde o radar pega

if velocidade2 > RADAR_2:
    print('A velocidade do carro excedeu o limite do Radar 02.')

if localCarro2 >= (LOCAL_2 - RADAR_RANGE2) and localCarro2 <= (LOCAL_2 + RADAR_RANGE2) and velocidade2 > RADAR_2:
    print('Você tomou uma multa pelo Radar 02.')
