__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao

experimentos = 10000
cont = 0

distri = Distribuicao()
for i in range(experimentos):
    resp = distri.binomial_simulada(5, 0.6)
    if resp >= 3:
        cont += 1
print("Probabilidade de obter no mínimo 3 sucessos é de aproximadamente %.4f" % (cont/experimentos))