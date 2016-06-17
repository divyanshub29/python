'''===Exponentiation==='''

def power(x,y):
    res=1
    while y>0:
        #condition for 'if' is to check wheteher y is odd or even
        if y&1:
            res=res*x
        #halving the value of y
        y=y>>1
        x=x*x

    return res

#this function calculates power of a number with complexity O(log(y))

print power(3,4)



'''====Modular Exponentiation==='''

def modpower(x,y,p):
    res=1

    x=x%p

    while y>0:

        if y&1:
            res=(res*x)%p

        y=y>>1
        x=(x*x)%p

    return res

print modpower(2,5,13)
#this function calculates power of a number with complexity O(log(y))
