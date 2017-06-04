def root(i):
    while arr[i]!=i:
        arr[i]=arr[arr[i]]
        i=arr[i]
    return i

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

# n vertices and m edges
n,m=map(int,raw_input().split())
arr=[i for i in xrange(n+1)]
size=[1]*(n+1)
edges=[]

for i in xrange(m):
    a,b,w=map(int,raw_input().split())
    edges.append([w,a,b,i+1])

edges.sort()
roots=[0]*(n+1)
result=[]
for i,edge in enumerate(edges,start=1):
    a=edge[1]
    b=edge[2]
    root_a=root(a)
    root_b=root(b)
    if root_a!=root_b:
        w_union(a,b)
        result.append(edge)

for edge in result:
    print 'edge from %d to %d having weight %d'%(edge[1],edge[2],edge[0])
