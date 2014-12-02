__author__ = 'anderson'
from random import randint

experimentos = 10000
cont = 0

for x in range(experimentos):
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    if dado1 + dado2 >= 4:
        if dado1 == 6 or dado2 == 6:
            cont += 1
            print(dado1,dado2)

print("Probabilidade: %.4f" % (cont/experimentos))