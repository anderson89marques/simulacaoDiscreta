__author__ = 'anderson'
import random

urna = ["vermelha","vermelha","vermelha","vermelha","vermelha","preta","preta"]
EXPERIMENTOS = 10000
CONT = 0.0

for x in range(EXPERIMENTOS):
    ficha1,ficha2 = "",""
    cpy_urna = urna.copy()

    #escolhendo as fichas
    ficha1 = random.choice(cpy_urna)
    cpy_urna.remove(ficha1)
    ficha2 = random.choice(cpy_urna)
    #fim escolhendo fichas

    print("fichas: %s :: %s" % (ficha1, ficha2))
    print(len(urna), len(cpy_urna))
    if ficha1 == ficha2:
        CONT += 1

print("Probabilidade: %.4f" % (CONT/EXPERIMENTOS))