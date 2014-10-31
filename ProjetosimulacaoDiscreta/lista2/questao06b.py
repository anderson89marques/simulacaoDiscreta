__author__ = 'anderson'

from  random import random
experimentos = 100000
cont = 0
pPecaA = 1/1000
pPecaB = 1/500
pPecaC = 1/200

for x in range(experimentos):#Lotes
    for i in range(10):#embalagens
        if random() <= pPecaA or random() <= pPecaB or random() <= pPecaC:
            cont += 1
            break

print(cont/experimentos)
