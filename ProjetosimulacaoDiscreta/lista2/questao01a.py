__author__ = 'andersonmarques'
from distributions.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()
prob = distri.binomialA(3, 0.6, 2)
print("probabilidade: %.4f" % prob)
