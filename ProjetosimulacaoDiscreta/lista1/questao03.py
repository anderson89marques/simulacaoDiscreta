__author__ = 'anderson'
from distributions.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()

r = distri.combinacao(10, 3) * distri.combinacao(9, 4)
print("Probabilidade: %.4f" % (r))

