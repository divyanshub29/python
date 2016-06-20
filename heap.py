def buildHeap(a):
    n=len(a)
    for i in range(n/2-1,-1,-1):
        heapify(a,i,n)



'''heapify make sure that parent node is larger than both children and if it is not then it perform swapping'''
def heapify(a,idx,maxIdx):
    left=2*idx+1
    right=2*idx+2
    if left < maxIdx and a[left]>a[idx]:
        largest=left
    else:
        largest=idx
    if right < maxIdx and a[right] > a[largest]:
        largest=right


    if largest !=idx:
        a[idx],a[largest]=a[largest],a[idx]
        heapify(a,largest,maxIdx)


def heapsort(a):
    buildHeap(a)
    for i in range(len(a)-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heapify(a,0,i)
a=[4,3,2,6,8,9,1,12,43,32]


def kthsmallest(collection,k):
    '''Retrun kth smallest element in collection for valid k >=1'''
    a=collection[:k]
    buildHeap(a)

    for i in range(k,len(collection)):
        if collection[i]<a[0]:
            a[0]=collection[i]
            heapify(a,0,k)
    return a[0]

print kthsmallest(a,3)
