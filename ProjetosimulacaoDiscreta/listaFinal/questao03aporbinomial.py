__author__ = 'anderson'

from distribuicoes.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()
experimentos = 10000
cont = 0
# m = lamb*tempo => 2/1 * 2 = 4
for x in range(experimentos):
    pt = distri.poisson_por_binomial(4)
    if pt >=3:
        cont += 1
print("%.4f" % (cont/experimentos))
