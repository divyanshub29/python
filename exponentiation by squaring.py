#Mathmeaticla algorithm

from time import time

def exponent(x,n):
    """Returns the value of x raised to the nth power"""


    if n==0:
        return 1
    if n==1:
        return x

    if n%2:
        return x*exponent(x*x,(n-1)/2)


    return exponent (x*x,n/2)

 
