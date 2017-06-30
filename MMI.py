# MMI --> Modular Multiplicative Inverse

# (A*B)%M = 1, B is inverse of A under modulo M
# Inverse exists only when A and M are co-prime ie. gcd(a,m)=1

# Approach 1 (Naive Approach)
def modinverse(a,m):
    a=a%m
    for b in xrange(1,m):
        if (a*b)%m==1:
            return b


# Approach 2, Using Extended Euclid
# Condition --> A and M are Co-Prime
def exgcd(a,b):
    prevx,x=1,0
    prevy,y=0,1
    while b:
        q=a/b
        x,prevx=prevx-q*x,x
        y,prevy=prevy-q*y,y
        a,b=b,a%b
    print x,y
    return a,prevx,prevy


def mulinv(b, n):
    g, x, y = exgcd(b, n)
    if g == 1: # Else Inverse doesn't exist as gcd(a,m) != 1
        return x % n

# Approach 3
# Only when M is Prime
# A' = A**(M-2) % M where A' denotes inverse of A

invA=pow(A,M-2,M)
    
