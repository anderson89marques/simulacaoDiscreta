__author__ = 'andersonmarques'
import random
from distribuicoes.distribuicoes_simulacao import Distribuicao

distri = Distribuicao()
#print(distri.y_max(100, 15))
print(1 - distri.monte_carloB())