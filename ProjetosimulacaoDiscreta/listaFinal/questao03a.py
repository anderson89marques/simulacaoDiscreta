__author__ = 'anderson'

from distribuicoes.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()
# m = lamb*tempo => 2/1 * 2 = 4
p012 = distri.poisson_analiticaB(4, 0, 2) #probab. x = 0, 1, 2
p = 1 - p012
print("%.4f" % p)

