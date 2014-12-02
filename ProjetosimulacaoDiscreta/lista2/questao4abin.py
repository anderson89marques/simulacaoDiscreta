__author__ = 'anderson'

from distributions.distribuicoes_simulacao import Distribuicao

experimentos = 10000
cont = 0

dist = Distribuicao()
for x in range(experimentos):
    resp = dist.poisson_por_binomial(3)
    if resp <= 2:
        cont += 1

print(cont/experimentos)
