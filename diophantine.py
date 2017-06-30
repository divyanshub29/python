# ax + by = c is a diophantine equation. In diphantine we only search integer
# solutions
"""
It has solution if and only if gcd(a,b)|c
If above condition holds then it will have infinitely many solutions and any
one solution can be used to generate all the other ones

all solutions are of the form
x = x1- r*b/gcd(a,b) and y = y1 + r*a/gcd(a,b) for some integer r.

https://math.stackexchange.com/questions/20717/how-to-find-solutions-of-linear-diophantine-ax-by-c
"""
def exgcd(a,b):
    prevx,x=1,0
    prevy,y=0,1
    while b:
        q=a/b
        x,prevx=prevx-q*x,x
        y,prevy=prevy-q*y,y
        a,b=b,a%b
    return a,prevx,prevy

# Let the given diophantine equation be of the form ax + by = c

a,b,c= 258, 147, 369
gcd,x1,y1=exgcd(a,b)

# Converting x1 and y1 according to c
x1,y1=x1*(c/gcd),y1*(c/gcd)

# all solutions are of the form x = x1- r*b/gcd and y = y1 + r*a/gcd
# Generate pairs of x and y

def pair(x1,y1,gcd,a,b,r):
    x=x1 + (b*r)/gcd
    y=y1 - (a*r)/gcd

    return x,y

# print x1,y1,gcd,a,b
# Alternate approach to generate pair
x=lambda r: x1 + (b*r)/gcd
y=lambda r: y1 - (a*r)/gcd
