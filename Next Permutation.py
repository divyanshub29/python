def next_permutation(arr):
    ''' print lexicographically next permutation of the given sequence
        Logic--> starting for reverse(i=n-1), find first pair where
        arr[i-1]<arr[i]. Now in range N to i-1 (startinf from N), find first
        element greater than arr[i-1] and swap them.Now reverse the array from
        i to n-1 and return the permutation which is required answer.
    '''
    n=len(arr)

    i=n-1

    while i>0:
        if arr[i]>arr[i-1]:
            j=n-1
            while j>=i:
                if arr[i-1]<arr[j]:
                    arr[i-1],arr[j]=arr[j],arr[i-1]
                    break
                j=j-1
            break
        i=i-1

    k=n-1
    while i<k:
        arr[i],arr[k]=arr[k],arr[i]
        i+=1
        k-=1

    return arr
