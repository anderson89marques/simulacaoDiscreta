__author__ = 'andersonmarques'

from distributions.distribuicoes_simulacao import Distribuicao


d = Distribuicao()
n = 100
p = 0.55
q = 1 - p

media = n*p
desvio = (n*p*q)**1/2
r = d.monte_carlo_fdp_normal(d.fdp_normal, media, desvio, 0, 60)
r2 = d.monte_carlo_fdp_normal(d.fdp_normal, media, desvio, 0, 45)
print("A probabilidade é de %.4f" % (r + r2))
