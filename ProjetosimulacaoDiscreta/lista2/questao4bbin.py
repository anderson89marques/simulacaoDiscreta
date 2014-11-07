__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao
experimentos = 10000
cont = 0

dist = Distribuicao()
for x in range(experimentos):
    resp = dist.poisson_por_binomial(3/3)
    if resp == 0:
        cont += 1

print(cont/experimentos)