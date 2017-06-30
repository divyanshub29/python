# Extended Euclid

# Recursive Approach
# Returns gcd,x and y
def extend(a,b):
    if b==0:
        gcd,x,y=a,1,0
        return gcd,x,y
    else:
        gcd,x,y=extend(b,a%b)
        x,y=y, x - y*(a/b)

    return gcd,x,y

print extend(16,10)


# Iterative Approach
# Returns gcd,x and y
def exgcd(a,b):
    prevx,x=1,0
    prevy,y=0,1
    while b:
        q=a/b
        x,prevx=prevx-q*x,x
        y,prevy=prevy-q*y,y
        a,b=b,a%b
    return a,prevx,prevy
