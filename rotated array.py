arra=[6,5,4,3,2,1]
arra=arra[::-1]
length=len(arra)/2

def smallest(a):
    low=0
    high=len(a)-1
    mid=(high +low)/2
    while low<=high:
        mid=((high +low)/2)
        
        
        if a[mid]>a[high]:
            low=mid+1
        elif a[mid]<a[high]:
            high=mid
        '''if a[mid]<a[high] and a[mid]<a[mid-1]:
            print a[mid]
            break
        ''' 
        if mid==high or mid==low:
            print a[mid]
            break
        
smallest(arra)
