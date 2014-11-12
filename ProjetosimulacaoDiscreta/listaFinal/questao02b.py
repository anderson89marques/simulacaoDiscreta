__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao

experimentos = 10000
cont = 0
distri = Distribuicao()
for x in range(experimentos):
    r = distri.binomial_simulada(40,0.58)

    if 15 <= r <= 20:
        cont += 1
print("%.4f" % (cont/experimentos))
