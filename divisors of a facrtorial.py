from math import sqrt
def sieve(n):
    primes = range(3, n + 1, 2) # primes above 2 must be odd so start at three and increase by 2
    for base in xrange(len(primes)):
        if primes[base] is None:
            continue
        if primes[base] > sqrt(n): # stop at sqrt of n
            break

        for i in xrange(base + (base + 1) * primes[base], len(primes), primes[base]):
            primes[i] = None
    primes.insert(0,2)
    return filter(None, primes)


#Count number of divisors
n=input()
primes=sieve(n+1)
result=1
for i in xrange(len(primes)):
    p=primes[i]
    exp=0
    while p<=n:
        exp=exp+(n/p)
        p=p*primes[i]
    result*=(exp+1)

print result
