__author__ = 'andersonmarques'
import random

experimentos = 10000
cont = 0

for i in range(experimentos):
    somadados = 0
    for x in range(3):
        somadados += random.randint(1, 6)

    if somadados >= 6 and somadados <= 13:
        cont += 1

print("Probabilidade é de %.4f" % (cont/experimentos))

#quantas formas os três somados são maiores ou iguais a 6 e menores ou iguais a 13
cardinalidade = 0
for j in range(1, 7):
    for k in range(1, 7):
        for l in range(1, 7):
           if j + l + k >= 6 and j + l + k  <= 13:
               cardinalidade += 1

print("Cardinalidade %4d" % (cardinalidade))