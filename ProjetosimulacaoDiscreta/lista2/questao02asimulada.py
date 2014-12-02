__author__ = 'andersonmarques'
from distributions.distribuicoes_simulacao import Distribuicao

experimentos = 10000
cont = 0

distri = Distribuicao()
for i in range(experimentos):
    r = distri.geometrica_simuladaGeral(4, 0.3)
    if r == 4:
        cont += 1
print("Probabilidade de obter sucesso exatamente no quarto ensaio é de aproximadamente %.4f" % (cont/experimentos))