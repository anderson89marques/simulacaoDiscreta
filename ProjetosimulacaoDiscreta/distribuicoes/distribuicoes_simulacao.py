__author__ = 'andersonmarques'

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
        r=0.0
        for x in range(k-1, n):
            r += self.binomialA(n, p, x+1)
        return r

    def geometrica(self, n, p):
        r = 1.0
        q = 1-p
        for x in range(n):
            if x < n - 1:
                r *= q
            else:
                r *= p
        return r