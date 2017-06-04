def construct(arr,n):
    #creating and initialzing all 0
    bitree=[0]*(n+1)

    #store the actual values in bitree using updatebit()
    for i in xrange(n):
        updatebit(bitree,n,i,arr[i])
        #updatebit(bitree,n,i+1,-arr[i])
    #print getsum(bitree,3)
    return bitree
    

#updates bitree of length n at index i with difference v
#if old value at bitree[i]=x
#then new value is bitree[i]=x+v
def updatebit(bitree,n,i,v):
    i+=1
    #traversing all ancestors and adding value 'v' to them
    while i<=n:
        bitree[i]+=v
        #below line takes 2's compliment then AND with the original number
        #and finally adds original number to it
        i+=i&(-i)


def getsum(bitree,i):
    #the value to returned (sum of required numbers)
    s=0
    #index of bitree is one more than the array
    i+=1

    while i>0:
        s+=bitree[i]

        #Moving index to parent node
        #i=i-(i&(-i))
        i-=i &(-i)
    return s

#Some function used in above functions

#To get index of parent node,used when returning sum 
def get_parent(child):
    return (child - (child & -child))

#Used when updating bitree
def get_next(index):
    return  (index + (index & -index))
arr=[0,0,2,4,1,8]
bitree=construct(arr,len(arr))
print getsum(bitree,2)






def query(i):
    ret=0
    while i>0:
        ret^=bit[i]
        i-=i&(-i)
    return ret

def update(i,val):
    while i<=n:
        bit[idx]^=val
        i+=i&(-i)

n,q=map(int,raw_input().split())
n=n+1
s=list(raw_input())
for i in xrange(n-1):
    update(i+1,1<<(ord(s[i])-97))
for _ in xrange(q):
    t,l,r=raw_input().split()
    if t=='1':
        l=int(l)
        aux=((1<<(ord(s[l])-97)^(1<<(ord(r)-97))))
        s[l]=r
        update(l,aux)
    else:
        l=int(l)-1
        r=int(r)
        print 'yes' if bin(query(r)^query(l)).count('1')<=1 else 'no'             
    
        


#BIT Range Query and Point Update

def update(n,i,v):
    i+=1
    while i<=n:
        bit[i]+=v
        i+=i&(-i)

def query(i):
    s=0
    while i>0:
        s+=bit[i]
        i-=i&(-i)
    return s
arr=map(int,raw_input().split())
bit=[0]*(n+1)
for i in xrange(n):
    update(n,i,arr[i])
   
        

#BIT Point Query and Range update
def update(n,i,v):
    i+=1
    while i<=n:
        bit[i]+=v
        i+=i&(-i)

def query(i):
    s=0
    while i>0:
        s+=bit[i]
        i-=i&(-i)
    return s
arr=map(int,raw_input().split())
n=len(arr)
bit=[0]*(n+1)
for i in xrange(n):
    update(n,i,arr[i])
    update(n,i+1,-arr[i])



# Range Update and Range Query
def update(arr,n,i,v):
    i+=1
    while i<=n:
        arr[i]+=v
        i+=i&(-i)
def r_update(a,b,v,n):
    update(b1,n,a,v)
    update(b1,n,b+1,-v)
    update(b2,n,a,v*(a-1))
    update(b2,n,b+1,-v*b)

def query(arr,b):
    add=0
    b+=1
    while b>0:
        add+=arr[b]
        b-=b&(-b)
    return add

def aux_query(b):
    return query(b1,b)*b - query(b2,b)

def r_query(a,b):
    return aux_query(b) - aux_query(a-1)

arr=map(int,raw_input().split())
n=len(arr)
b1=[0]*(n+1)
b2=[0]*(n+1)


# While updating first time don't update using update function instead use
# r_update because b2 also needs to be updated accordingly

for i in xrange(n):
    r_update(i,i,arr[i],n)

















































