# Disjoint Set Union (DSU), type of union-> weighted(ie. size of set)

# Function to find root of an element
def root(i):
    ''' returns root/representative of the set'''
    while arr[i]!=i:
        arr[i]=arr[arr[i]]
        i=arr[i]
    return i

# Weighted Union
def w_union(a,b):
    root_a=root(a)
    root_b=root(b)
    if root_a!=root_b:
        if size[root_a]<size[root_b]:
            arr[root_a]=arr[root_b]
            size[root_b]+=size[root_a]
        else:
            arr[root_b]=arr[root_a]
            size[root_a]+=size[root_b]

# Number of Vertices
vertices=input()

# Array to store parent of an element (which eventually lead to root of set)
arr=[i for i in xrange(vertices+1)]

# Array to store size of set to which the element belong,element is represented
# by index here ie. element==index
size=[1]*(vertices+1)

#
edges=input()
for i in xrange(edges):
    # edge between a and b
    a,b=map(int,raw_input().split())
    #union of edges
    w_union(a,b)
