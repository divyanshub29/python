def isPrime(n):
    if n <=1:
        return False
    if n<=3:
        return True

    if n%2==0 or n%3==0:
        return False

    i=5
    j=i*i
    while j <= n:
        if n%i==0 or n%(i+2)==0:
            return False

        i=i+6

    return True



print isPrime(11)
print isPrime(15)
