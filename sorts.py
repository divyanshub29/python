''' insertion sort '''

def insertion(A):
    for i in range(1,len(A)):
        insert(A,i,A[i])


def insert(A,idx,value):
    i=idx-1
    while i>=0 and A[i] > value:
        A[i+1]=A[i]
        i=i-1

    A[i+1]=value

'''indertion sort ends'''


'''Merge sort '''

def copymergesort(A):
    if len(A) < 2:
        return A



    mid=len(A)/2
    left=mergesort(A[:mid])
    right=mergesort(A[mid:])

    i,j=0,0
    B=[]

    while len(B)<len(A):
        if j>=len(right) or (i<mid and left[i]<right[j]):
            B.append(left[i])
            i +=1
        elif j<len(right):
            B.append(right[j])

            j+=1

    return B


''' merge sort ends'''




'''MERGESORT'''

def mergesort(A):
    '''merge sort A in place'''
    copy=list(A)
    mergesort_array(copy,A,0,len(A))


def mergesort_array(A,result,start,end):

    if end-start < 2:
        return
    if end-start==2:
        if result[start]>result[start+1]:
            result[start],result[start+1]=result[start+1],result[start]
        return


    mid=(end+start)/2
    mergesort_array(result,A,start,mid)
    mergesort_array(result,A,mid,end)


    i=start
    j=mid
    idx=start
    while idx<end:
        if j>= end or (i<mid and A[i] < A[j]):
            result[idx]=A[i]
            i +=1
        else:
            result[idx]=A[j]
            j +=1
        idx +=1


a=[2,1,3,9,87,6,5,5,4]
mergesort(a)
print a





'''======QUICK SORT======='''''

#a-->array si-->startind index ei-->ending index

def quicksort(a,si,ei):
    if si<ei:
        pi=partition(a,si,ei)
        quicksort(a,si,pi-1)
        quicksort(a,pi+1,ei)

def partiton(a,si,ei):
    x=a[ei]
    i=si-1
    for j in range(si,ei):
        if a[j] <=x:
            i+=1

            a[i],a[j]=a[j],a[i]
        a[i+1],a[ei]=a[ei],a[i+1]
    return i+1




