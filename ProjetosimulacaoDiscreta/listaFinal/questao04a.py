__author__ = 'anderson'

from distribuicoes.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()

p = distri.poisson_analiticaB(20, 18, 25)

print("%.4f" % p)
