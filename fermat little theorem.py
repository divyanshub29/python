from random import *
'''
def carmichael(n):
    arr=[561,1105,1729,2465,2821,6601,8911,41041,62745,63973,75361,101101,126217,172081,188461,278545,340561]
    if n in arr:
        return True

    return False

'''
def fermat(n,k=5):


    if n==2 or n==3:
        return True

    if n%2==0 or n<=1:
        return False
    
'''
    if carmichael(n)==True:
        return False
'''

    for i in xrange(k):
        a=randint(2,n-1)


        if pow(a,n-1,n) != 1:
            return False

    return True


print fermat(11,3)
print fermat(561,1)


'''there exist some composite numbers which passes the fermat's test.
    Such numbers ar called Carmichael numbers.

    some of the carmichael numbers are:
    [561,1105,1729,2465,2821,6601,8911,41041,62745,63973,75361,101101,126217,172081,188461,278545,340561]
'''
'''when testing for smal prime numbers, just uncomment the carmichael function and calling of carmichael in fermata and set k=1.'''

