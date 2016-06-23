   
from math import sqrt

def sieveOfEratosthenes(n):
    primes = range(3, n + 1, 2) # primes above 2 must be odd so start at three and increase by 2
    for base in xrange(len(primes)):
        if primes[base] is None:
            continue
        if primes[base] >= sqrt(n): # stop at sqrt of n
            break

        for i in xrange(base + (base + 1) * primes[base], len(primes), primes[base]):
            primes[i] = None
    primes.insert(0,2)
    return filter(None, primes)

arr=((sieveOfEratosthenes(550)))#change the number as per requirement

i=1
for item in arr:
    print i,
    print " ",
    print item
    i=i+1
