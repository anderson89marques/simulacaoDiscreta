__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()

r = distri.hipergeometrica(10, 3, 9, 4)
print("Probabilidade: %.4f" % (r))
