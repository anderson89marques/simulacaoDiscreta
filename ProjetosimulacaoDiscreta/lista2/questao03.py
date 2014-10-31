__author__ = 'anderson'
from random import randint
experimentos = 10000
cont = 0

for x in range(experimentos):
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    if dado1 + dado2 > 6:
        if dado1 == 5 or dado2 == 5:
            cont += 1
print("A probabilidade de sair pelo menos uma 5 dado que a soma dos dois dados é 6: %.4f" % (cont/experimentos))
