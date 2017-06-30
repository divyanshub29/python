# Modulo Techniques

# 1) (A/B)%Mod = (A%(Mod*B))/B
# Conditions --> None
# Use Case --> when B is not co-prime with Mod
# Code
res= (A%(Mod*B))/B


# 2) (A/B)%Mod = ((A%Mod) * B**(phi(Mod)-1) %Mod )%Mod
# Conditions --> B and Mod are co-prime
# Proof--> Derived Using Euler's theorem which states that B**phi(Mod)%Mod = 1
# Code
from fractions import gcd
def phi(n):
    result=1
    for i in xrange(2,n+1):
        if gcd(i,n)==1:
            result+=1
    return result
res=((A%Mod)*pow(B,phi(Mod)-1,Mod))%Mod




# 3) (A/B)%Mod = ((A%Mod) * (B**(Mod-2))%Mod)%Mod
# Conditions --> B and Mod are co-prime and Mod is a prime Number
# Code
res=((A%Mod) * pow(B,Mod-2,Mod))%Mod


# 4) A**N%Mod = A**(N%phi(Mod)) % Mod
# Conditions --> A and Mod are co-prime
# Code
from fractions import gcd
def phi(n):
    result=1
    for i in xrange(2,n+1):
        if gcd(i,n)==1:
            result+=1
    return result

res=pow(A,N%phi(Mod),Mod)



# 5) (A*B)%Mod, where Mod can't be represented using int (Mainly for CPP)
def mulmod(A,B,Mod):
    res=0
    while B>0:
        if B%2==1:
            res = (res + A)%Mod
        A = (A*2)%Mod
        B=B/2
    return res
