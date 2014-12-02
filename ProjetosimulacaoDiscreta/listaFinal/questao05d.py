__author__ = 'andersonmarques'
from distributions.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()
r = (1 - distri.monte_carlo_fdp_normal(distri.fdp_normal, 6, 2.5, 0, 8)) * 100
x = 1000 * r / 100
print("Número estimado de pessoas com nota 8: %d" % x)

