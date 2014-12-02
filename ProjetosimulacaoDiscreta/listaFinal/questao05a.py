__author__ = 'andersonmarques'

from distributions.distribuicoes_simulacao import Distribuicao


distri = Distribuicao()
print("%.4f" % (1 - distri.monte_carlo_fdp_normal(distri.fdp_normal, 6, 2.5, 0, 6)))
