__author__ = 'anderson'

from distributions.distribuicoes_simulacao import Distribuicao

dist = Distribuicao()
resp = 0
n = 100
M = 10
for x in range(6, 10):
    resp += dist.hipergeometrica(M, x, n-M, M-x)
print(resp)
