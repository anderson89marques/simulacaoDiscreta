__author__ = 'anderson'
from distributions.distribuicoes_simulacao import Distribuicao

dist = Distribuicao()
resp = dist.poisson_analiticaB(3, 0, 2)
print(resp)