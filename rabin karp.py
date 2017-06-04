'''===Rabin-Karp==='''
#txt->text
#pat->pattern
#q-> a prime number,take a sufficiently large number
def rabin(pat,txt,q):
    d=256 #set of characters used in text
    m,n=len(pat),len(txt)
    i=j=0
    p=t=0 #p,t are has value of pattern and text respectively

    #value of h
    h=pow(d,m-1,q)

    #calculating the hash value of pattern and first window of text
    for i in xrange(m):
        p=(d*p + ord(pat[i]))%q
        t=(d*q+ord(txt[i]))%q

    #sliding the pattern over text one by one
        for i in xrange(n-m+1):
            if p==t:
                for j in xrange(m):
                    if txt[i+j] != pat[j]:
                        break
                j+=1
                if j==m:
                    print "pattern found at index %d"%(i)
            if i<n-m:
                t=(d*(t-ord(txt[i])*h))+ord(txt[i+m])%q
                if t<0:
                    t+=q
        

    
