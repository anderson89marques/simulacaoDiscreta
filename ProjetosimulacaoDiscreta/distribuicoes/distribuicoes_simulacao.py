__author__ = 'andersonmarques'
import random

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
            print("%f : %d" %(c, x+1))
            r += c
        return r

    #retorna o número de sucessos
    def binomial_simulada(self, n, p,):
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
        for i in range(1, n+1):
            if random.uniform(0, 1) <= p and i == n:
                sucesso = True
        return sucesso



    def hipergeometrica(self, M, m, E, e):
        return self.combinacao(M, m) * self.combinacao(E, e)/ self.combinacao(M+E, m+e)