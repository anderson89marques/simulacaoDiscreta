__author__ = 'anderson'
from distributions.distribuicoes_simulacao import Distribuicao


experimentos = 10000
cont = 0
dist = Distribuicao()

for x in range(experimentos):
    r = dist.geometrica_simuladaGeral(5, 0.3)
    if r < 5:
        cont += 1

print("Probabilidade de obter sucesso antes do 5 ensaio é de aproximadamente %.4f" % (cont/experimentos))


