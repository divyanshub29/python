def binarysearch(a,t):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)/2
        if t==a[mid]:
            print mid
            return True
        elif t<a[mid]:
            high=mid-1
        else:
            low=mid+1
    return False


arr=[1,5,6,7,8,9,11,23,45,56]
print binarysearch(arr,11)
print binarysearch(arr,9)
print binarysearch(arr,10)
