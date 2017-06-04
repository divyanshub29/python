#Detect if Two integers have opposite signs
x,y=5,10
f=(x^y)<0

#Minimum(x,y)
r = y ^ ((x ^ y) & -(x < y))
#Maximum(x,y)
r = x ^ ((x ^ y) & -(x < y))

#determine if integer is a power of 2
result=v and not(v & (v - 1))

#set bits in O(k) where k=number of set bits
v=20
count=0
while v:
    v=v&(v-1)
    count+=1

#Swapping with XOR
a,b=5,7
a^=b
b^=a
a^=b

#check if ith bit is set
n=10
if n &(1<<i):
    return True
else:
    return False

#set ith bit
n=20
n=n|(1<<i)


#Powerset
arr=[2,3,4,5]
n=4
for i in range(1<<n):
    for j in range(n):
        if i&(1<<j):
            print arr[j],
    print

#returns rightmost 1 in binary representation of x
def rightmost(x):
    return x^(x&(x-1))

#aliter
def rightmost2(x):
    return x&(-x)

#next power of 2
#if n is power of 2 itself then returns n
def next_power_of_2(n):
    if n == 0:
        return 1
    if n & (n - 1) == 0:
        return n
    while n & (n - 1) > 0:
        n &= (n - 1)

    return n << 1
