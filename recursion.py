def listsum(arr):
        if len(arr)==1:
                return arr[0]
        else:
                return arr[0]+ listsum(arr[1:])

art=[1,2,3,4,5,6,7,8,9,0]
listsum(arr)
