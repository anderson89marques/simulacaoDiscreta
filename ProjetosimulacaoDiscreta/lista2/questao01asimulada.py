__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao

experimentos = 10000
cont = 0

distri = Distribuicao()
for i in range(experimentos):
    resp = distri.binomial_simulada(3, 0.6)
    if resp == 2:
        cont += 1
print("Probabilidade de obter exatamente 2 sucessos é de aproximadamente %.4f" % (cont/experimentos))
