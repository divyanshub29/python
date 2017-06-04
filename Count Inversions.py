# Count Inversions in an array using merge sort in O(N*logN) ( Divide and Conquer )
# Sorts the array and also stores the number of inversions in global variable count
count=0
def mergesort(arr):
    global count
    if len(arr)>1:
        mid=len(arr)/2
        lhalf=arr[:mid]
        rhalf=arr[mid:]
        mergesort(lhalf)
        mergesort(rhalf)
        i=j=k=0

        while i<len(lhalf) and j<len(rhalf):
            if lhalf[i]<=rhalf[j]:
                arr[k]=lhalf[i]
                i+=1
            else:
                count+=len(lhalf)-i
                arr[k]=rhalf[j]
                j+=1
            k+=1

        while i<len(lhalf):
            arr[k]=lhalf[i]
            #count+=1
            i+=1
            k+=1

        while j<len(rhalf):
            arr[k]=rhalf[j]
            j+=1
            k+=1


#arr=[6,5,4,3,2,1]
arr=[1,3,2,5,4,6]
mergesort(arr)
print count
