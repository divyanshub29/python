# Input Array
arr=map(int,raw_input().split())

# Length of input array
n=len(arr)

# Segment Tree, in worst case it requires 4*n memory.
seg=[0]*(4*n+2)

# Lazy array, initialized with all zeroes as seg is also 0 inititalized
lazy=list(seg)

# Function to Build Segment Tree
def build(node,start,end):
    if start==end:
        seg[node]=arr[start]
    else:
        mid=(start+end)/2
        build(2*node,start,mid)
        build(2*node+1,mid+1,end)
        seg[node]=seg[2*node]+seg[2*node+1]

        
# Here "val" is the difference between old and current value
# For eg. if old value was 3 and new val is 5 then val is (5-3) =2
# idx is index int he array to be updated.
# This update function doesn't use lazy Propagation.
def update(node,start,end,idx,val):
    if start==end:
        # arr[idx]+=val
        seg[node]+=val
    else:
        mid=(start+end)/2
        if start<=idx and idx<= mid:
            update(2*node,start,mid,idx,val)
        else:
            update(2*node+1,mid+1,end,idx,val)
        seg[node]=seg[2*node]+seg[2*node+1]

        
# query in range l to r
# This query function doesn't use Lazy Propagation.
def query(node,start,end,l,r):
    if r<start or end<l:
        return 0
    if l<=start and end<=r:
        return seg[node]

    mid=(start+end)/2
    p1=query(2*node,start,mid,l,r)
    p2=query(2*node+1,mid+1,end,l,r)
    return p1+p2


# This Range Update function doesn't use Lazy Propagation.
def update_range(node,start,end,l,r,val):
    if start>end or start>r or end<l:
        return
    if start==end:
        seg[node]+=val
        return
    mid=(start+end)/2
    update_range(node*2,start,mid,l,r,val)
    update_range(node*2+1,mid+1,end,l,r,val)
    seg[node]=seg[node*2]+seg[node*2+1]


""" ------------- LAZY PROPAGATION--------------"""    

# Instead of using query and update functions written above,
# these lazy functions can be used for better performance

# Lazy Update function, efficient than simple update function
# For point update purpose, pass same value to l and r i.e. l==r
def lazy_update(node,start,end,l,r,val):
    if lazy[node]!=0:
        seg[node]+=(end-start+1)*lazy[node]
        if start!=end:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0

    if start>end or start>r or end<l:
        return

    if start>=l and end<=r:
        seg[node]+=(end-start+1)*val
        if start!=end:
            lazy[node*2]+=val
            lazy[node*2+1]+=val
        return
    mid=(start+end)/2
    lazy_update(node*2,start,mid,l,r,val)
    lazy_update(node*2+1,mid+1,end,l,r,val)
    seg[node]=seg[node*2]+seg[node*2+1]

# Lazy Query function
def lazy_query(node,start,end,l,r):
    if start>end or start>r or end<l:
        return 0

    if lazy[node]!=0:
        seg[node]+=(end-start+1)*lazy[node]
        if start!=end:
            lazy[node*2]+=lazy[node]
            lazy[node*2+1]+=lazy[node]
        lazy[node]=0

    if start>=l and end<=r:
        return seg[node]
    mid=(start+end)/2
    p1=lazy_query(node*2,start,mid,l,r)
    p2=lazy_query(node*2+1,mid+1,end,l,r)
    return p1+p2



