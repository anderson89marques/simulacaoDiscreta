__author__ = 'andersonmarques'
import math

from distributions.distribuicoes_simulacao import Distribuicao

def funcao(x, lamb=1):
    return math.exp(-x**2)

def funca(x, lamb=1):
    return 2*x

distri = Distribuicao()
print(distri.monte_carlo(funcao, 2, 3, 1))

