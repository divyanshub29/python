def primefactors(n):
    while n%2==0:
        print 2,
        n=n/2
    i=3
    while i<=int(n**0.5):

        while n%i==0:
            print i,
            n=n/i

        i=i+2 #n is odd therefore i+2 not i+1


    if n>2:
        print n
primefactors(315)
