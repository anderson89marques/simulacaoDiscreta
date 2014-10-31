__author__ = 'andersonmarques'
import random
import math

class Distribuicao:
    def combinacao(self, n, k):
        return self.fat(n)/(self.fat(k)*self.fat(n-k))

    def fat(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.fat(n-1)

    def binomialA(self, n, p, k):
        r = 1.0
        q = 1-p
        for x in range(n):
            if x < k:
                r *= p
            else:
                r *= q
        return self.combinacao(n, k) * r

    #no mínimo k sucessos
    def binomialB(self, n, p, k):
        r = 0.0
        for x in range(k-1, n):
            c = self.binomialA(n, p, x+1)
            r += c
        return r

    #retorna o número de sucessos
    def binomial_simulada(self, n, p):
        cont = 0
        for i in range(n):
            if random.uniform(0, 1) <= p:
                cont += 1
        return cont

    def geometrica(self, n, p):
        r = 1.0
        q = 1-p
        for x in range(n):
            if x < n - 1:
                r *= q
            else:
                r *= p
        return r

    #antes do n-ésimo ensaio
    def geometricaB(self, n, p):
        r = 0.0
        for x in range(n-1):
            c = self.geometrica(x+1, p)
            print("%f : %d" %(c, x+1))
            r += c
        return r

    def geometrica_simulada(self, n, p):
        sucesso = False
        ok = True
        for i in range(1, n+1):
            r = random.uniform(0, 1)
            if r <= p and i < n:
                ok = False
            if r <= p and i == n and ok:
                sucesso = True
        return sucesso

    #retorna em qual ensaio que aconteceu o sucesso
    def geometrica_simuladaGeral(self,n ,p):
        k = n+1 #caso só tenha insucesso, retorna um valor acima de n
        for i in range(1, n+1):
            r = random.uniform(0, 1)
            if r <= p:
                k = i
                break
        return k

    def poisson_analitica(self,lamb, k):
        return ((lamb**k) * math.exp(-lamb)) / self.fat(k)

    def poisson_analiticaB(self, lamb, k1, k2):
        r = 0
        for x in range(k1, k2+1):
            r += self.poisson_analitica(lamb, x)
        return r

    def poisson_por_binomial(self, lamb):
        n = 1500 #n grande
        p = lamb/n
        return self.binomial_simulada(n, p)


    def hipergeometrica(self, M, m, E, e):
        return self.combinacao(M, m) * self.combinacao(E, e)/ self.combinacao(M+E, m+e)