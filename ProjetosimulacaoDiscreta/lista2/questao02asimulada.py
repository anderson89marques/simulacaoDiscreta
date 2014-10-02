__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao

experimentos = 10000
cont = 0

distri = Distribuicao()
for i in range(experimentos):
    if distri.geometrica_simulada(4, 0.3):
        cont += 1
print("Probabilidade de obter sucesso exatamente no quarto ensaio é de aproximadamente %.4f" % (cont/experimentos))