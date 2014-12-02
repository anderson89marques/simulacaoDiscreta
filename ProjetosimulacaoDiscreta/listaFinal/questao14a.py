__author__ = 'andersonmarques'
from distributions.distribuicoes_simulacao import Distribuicao
d = Distribuicao()

experimentos = 10000
cont = 0

#for x in range(experimentos):
r = d.binomialC(100, 0.55, 45, 60)
print(r)