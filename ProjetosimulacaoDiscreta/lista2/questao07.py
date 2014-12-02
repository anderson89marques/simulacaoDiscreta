__author__ = 'anderson'
from random import randint

urnaA = [5,5,5,5,6,6,7,8]
tamA = len(urnaA)
urnaB = [4,4,5,8,9]
tamB = len(urnaB)
soma = 0

for x in range(101):
    a = urnaA[randint(0, tamA-1)]
    b = urnaB[randint(0, tamB-1)]
    soma += a
    soma -= b

if soma > 0:
    print("Você ganhou %d reais"%soma)
elif soma < 0:
    print("Você perdeu %d reais"%soma)
else:
    print("Você não ganhou nem perdeu")