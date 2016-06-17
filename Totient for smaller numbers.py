def computeTotient(n):
    phi=[0]*(n+1)
    i=1
    while i<=n:
        phi[i]=i
        i=i+1


    p=2
    while p<=n:
        if phi[p]==p:
            phi[p]=p-1

            i=2*p
            while i<=n:
                phi[i]=(phi[i]/p)*(p-1)
                i+=p
        p+=1


    i=1
    while i<=n:
        print "Totient of",
        print i,
        print "is",
        print phi[i]
        i+=1


computeTotient(12)



'''
Algorithm for thi function is
1) Create an array phi[1..n] to store totient(phi) values of all numbers 
   from 1 to n.  

2) Initialize all values such that phi[i] stores i.  This
   initialization serves two purposes.
   a) To check if phi[i] is already evaluated or not. Note that
      the maximum possible phi value of a number i is i-1.
   b) To initialize phi[i] as i is a multiple in above product
      formula. 

3) Run a loop for p = 2 to n
    a) If phi[p] is p, means p is not evaluated yet and p is a 
       prime number (slimier to Sieve), otherwise phi[p] must 
       have been updated in step 3.b
    b) Traverse through all multiples of p and update all 
       multiples of p by multiplying with (1-1/p).

4) Run a loop from i = 1 to n and print all Ph[i] values.
'''
