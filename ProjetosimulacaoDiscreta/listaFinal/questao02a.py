__author__ = 'andersonmarques'


from distributions.distribuicoes_simulacao import Distribuicao


distri = Distribuicao()

print("%.4f" % distri.binomialA(40, 0.58, 25))
