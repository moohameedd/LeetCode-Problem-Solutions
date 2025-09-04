class Solution:
    def countPrimes(self, n: int) -> int:
        def soe(x):
            prime=[False] * (x+1)
            res=set()
            for i in range(2,x+1):
                if not prime[i] :
                    res.add(i)
                if i**2<=x:
                    for j in range(i,x+1,i):
                        prime[j]=True
            return res
        primes=soe(n-1)
        return len(primes)
        