__author__ = 'anderson'
import random

urna0 = ["v", "v", "p"]
urna1 = ["v", "v", "v", "v", "v", "p", "p"]
urna2 = ["p", "p", "p", "p", "p", "v"]
urnas = [urna0, urna1, urna2]
experimentos = 10000
cont = 0

for x in range(experimentos):
    r = random.randint(0, 2)

    #pegando a urna
    urna = urnas[r]
    cor = random.choice(urna)
    if cor == "v" and r == 2:
        cont += 1

print("Probabilidade: %.4f" % (cont/experimentos))
