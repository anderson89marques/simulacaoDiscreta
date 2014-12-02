__author__ = 'anderson'
from distributions.distribuicoes_simulacao import Distribuicao

dist = Distribuicao()
resp = dist.poisson_analiticaB(3/3, 0, 0)
print(resp)