__author__ = 'andersonmarques'

from distributions.distribuicoes_simulacao import Distribuicao


distri = Distribuicao()
print("Pessoas com 9.4 representam aproximadamente %.4f por cento do total" % ((1 - distri.monte_carlo_fdp_normal(distri.fdp_normal, 6, 2.5, 0, 9.4)) * 100))
print("Portanto provavelmente essa e a nota minima para conseguir a bolsa.")
