__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()
prob = distri.binomialB(5, 0.6, 3)
print("probabilidade: %.4f" % prob)

