__author__ = 'andersonmarques'

from distribuicoes.distribuicoes_simulacao import Distribuicao

d = Distribuicao()
n = 100
p = 0.55
q = 1 - p

media = n*p
print("media: %.4f" % media)
desvio = (n*p*q)**1/2
print("desvio: %.4f" % desvio)
r = d.monte_carlo_fdp_normal(d.fdp_normal, media, desvio, 0, 60)
r2 = d.monte_carlo_fdp_normal(d.fdp_normal, media, desvio, 0, 45)

print("%.4f" % r)
print("%.4f" % r2)
print("%.4f" % (r - r2))