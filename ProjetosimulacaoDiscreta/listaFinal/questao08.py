__author__ = 'anderson'

from datetime import date
from random import randint

experimentos = 10000
cont = 0
num_pessoas = 23

for x in range(experimentos):
    hoje = date.today()
    datas = [date.fromordinal(hoje.toordinal() - randint(365, 20*365)) for _ in range(num_pessoas)] #escolhe datas aleatórias entre 1 e 20 anos atrás

    for i,y in enumerate(datas):
        for x in datas[i+1:]:
            if y.day == x.day and y.month == x.month:
                cont += 1
                break

print(cont/experimentos)