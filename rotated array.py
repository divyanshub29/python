'''
arra=[6,5,4,3,2,1]
#arra=arra[::-1]
#arra=[5,6,7,8,9,1,2,3,4]
#arra=[1,2,3,4]
length=len(arra)/2

def smallest(a):
    low=0
    high=len(a)-1
    mid=(high +low)/2
    while low<=high:
        mid=((high +low)/2)
        #print mid
        
        if a[mid]>a[high]:
            low=mid+1
        elif a[mid]<a[high]:
            high=mid
        if mid<len(a)-1:
            if a[mid]<a[mid+1] and a[mid]<a[mid-1]:
                print a[mid]
                break
            
        if mid==len(a)-1 or mid==0:
            print a[mid]
            break
        
smallest(arra)
'''
import random
arr=[]
for _ in xrange(50):
    arr.append(random.randint(1,100))
arr=sorted(arr)
minimum=arr[0]
print arr
print 'min value',
print minimum
def smallest_with_repeated(a):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)/2
        #print "Mid Low High",
        #print mid,low,high
        if a[mid]>a[high]:
            low=mid+1
        elif a[mid]<a[high]:
            high=mid
        if mid<len(a)-1 and a[mid]<a[mid+1] and a[mid]<a[mid-1]:
                return a[mid]
        if mid==len(a)-1 or mid==0:
            return a[mid]
        if (mid==low or mid==low+1) and (mid==high or mid==high-1) and a[mid]<=a[low] and a[mid]<=a[high]:
            return a[mid]
def smallest(a):
    low=0
    high=len(a)-1
    mid=(high +low)/2
    while low<high:
        mid=((high +low)/2)
        '''
        print 'mid',
        print mid
        print "low,high",
        print low,high'''
        
        if a[mid]>a[high]:
            low=mid+1
        elif a[mid]<a[high]:
            high=mid
        if mid<len(a)-1:
            if a[mid]<=a[mid+1] and a[mid]<a[mid-1]:
                return a[mid]
                break
            elif a[mid]==a[mid+1] and a[mid]==a[mid-1]:
                return a[mid]
                break
        if mid==len(a)-1 or mid==0:
            #print 'last condition',
            return a[mid]
            break


for _ in range(20):
    k=random.randint(1,49)
    art=arr[k:]+arr[:k]
    #print art
    x=smallest_with_repeated(art)
    if x==minimum:
        print "TRUE"
    else:
        print x,minimum,
        print "FALSE"
