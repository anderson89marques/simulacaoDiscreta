__author__ = 'anderson'
from distributions.distribuicoes_simulacao import Distribuicao
import random

fila =[]
amostras_tempo = []
r = random.random()
dist = Distribuicao()
tempo_servico = 5/60 #5min em horas
proximaChegada = dist.fdp_exponencial(15, random.random())
proximaSaida = proximaChegada + tempo_servico

for x in range(1000000):
    if proximaChegada < proximaSaida:
        fila.append(proximaChegada)
        proximaChegada += dist.fdp_exponencial(15, random.random())
    else:
        tempo = proximaSaida - fila.pop(0)
        amostras_tempo.append(tempo)

        if len(fila) == 0:
            proximaSaida = proximaChegada + tempo_servico
        else:
            proximaSaida += tempo_servico

print(len(amostras_tempo), len(fila))