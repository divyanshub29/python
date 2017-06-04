
def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


#print max_subarray(A)

def kadane(arr):
    a=b=0
    for x in arr:
        a=max(0,a+x)
        b=max(b,a)
        print a,b
    return b


# Print Max subarray with Start and End indices

arr=[-2, -3, 4, -1, -2, 1, 5, -3]
a=0
b=arr[0]
start=end=s=0
for i,x in enumerate(arr):
    a+=x
    if b<a:
        b=a
        start=s
        end=i
    if a<0:
        a=0
        s=i+1



print b
print start,end
