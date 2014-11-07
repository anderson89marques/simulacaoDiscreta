__author__ = 'andersonmarques'
from random import randint

experimentos = 10000
cont = 0

for x in range(experimentos):
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    dado3 = randint(1, 6)
    if 9 <= dado1 + dado2 + dado3 <= 15:
        if dado1 == 6 and dado2 != 6 and dado3 != 6:
            cont += 1
        elif dado2 == 6 and dado1 != 6 and dado3 != 6:
            cont += 1
        elif dado2 == 6 and dado1 != 6 and dado3 != 6:
            cont += 1

print("Probabilidade: %.4f" % (cont/experimentos))