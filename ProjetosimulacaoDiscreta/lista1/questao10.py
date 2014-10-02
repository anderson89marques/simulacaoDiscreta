__author__ = 'andersonmarques'
import random
#1 = cara, 2 = coroa
experimentos = 10000
cont = 0
for x in range(experimentos):
    contcara = 0
    contcoroa = 0
    for i in range(100):
        if random.randint(1, 2) == 1:
            contcara += 1
        else:
            contcoroa += 1
    if contcara == 40:
        cont += 1
print("probabilidade %.4f" % (cont/experimentos))