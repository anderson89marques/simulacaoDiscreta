__author__ = 'andersonmarques'

from distributions.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()

print(1-distri.monte_carlo(distri.fdp_exponencial, 0, 2300, 1/2000))
