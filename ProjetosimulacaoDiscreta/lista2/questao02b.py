__author__ = 'andersonmarques'

from distributions.distribuicoes_simulacao import Distribuicao
distri = Distribuicao()
prob = distri.geometricaB(5, 0.3)
print("probabilidade: %.4f" % prob)
