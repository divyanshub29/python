
"""
Suppose n1, n2, . . . nk are positive integers that are pairwise co-prime.

Then, for any given sequence of integers a1, a2, . . . , ak
there exists an integer x solving the following system of
simultaneous congruences:

            x ≡ a 1 ( mod n1 )
            x ≡ a 2 ( mod n2 )
                 ⋮
            x ≡ a k ( mod nk )


Furthermore, all solutions x of this system are congruent modulo the product,
 N = n1 n2 . . . nk

x=∑i=1naibib′i(modM)
x= Summation from i=1 to n of ai*bi*bi' where ai is given, bi is prod/ni
and bi' is modulo multiplicative inverse of bi
"""
# Extended Exuclid
def exgcd(a,b):
    prevx,x=1,0
    prevy,y=0,1
    while b:
        q=a/b
        x,prevx=prevx-q*x,x
        y,prevy=prevy-q*y,y
        a,b=b,a%b
    return a,prevx,prevy

# Modulo Multiplicative Inverse
def mul_inv(b, m):
    n=m
    g, x, y = exgcd(b, n)
    if g == 1: # Else Inverse doesn't exist as gcd(a,m) != 1
        return x % n

# Chinese Remainder Theorem, n is list of n1, n2, . . . nk and
# similarly a is a list of a1, a2, . . . ak
def crt(n, a):
    add = 0
    prod = reduce(lambda a, b: a*b, n) # Product of all numbers
    length=len(n) # Length of array n
    for i in xrange(length): # Summation Formula
        p = prod / n[i]
        add += a[i] * mul_inv(p, n[i]) * p
    return add % prod # Final Answer

n=[3,5,7]
a=[2,3,2]

# print crt(n,a), expected value is 23
