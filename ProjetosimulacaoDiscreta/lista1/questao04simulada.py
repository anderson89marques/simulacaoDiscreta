__author__ = 'anderson'
import random

profissionais = ["m","m","m","m","m","m","m","m","m","m","e","e","e","e","e","e","e","e","e"]
cpy_profissionais = []
experimentos = 10000
contM = 0
contE = 0
cont = 0

for x in range(experimentos):
    cpy_profissionais = profissionais.copy()
    for i in range(7):
        prof = random.choice(cpy_profissionais)
        if prof == "m":
            contM += 1
        else:
            contE += 1
        cpy_profissionais.remove(prof)
    if contM == 3 and contE == 4:
        cont += 1
    contM, contE = 0, 0

print("Probabilidade: %.4f" % (cont/experimentos))