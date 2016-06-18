'''====Euler's Totient Function==='''

'''APPROACH 1: O(nlogn) '''
def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)






def totient(n):
    result=1
    i=2
    while i<=n:
        if gcd(i,n)==1:
            result+=1

        i=i+1

    return result



print totient(9)


