#Topological sort
#graph
#number of nodes
n=input()
nodes=[i for i in xrange(n)]
alist=[[] for _ in xrange(n)]
edges=input()
for i in xrange(edges):
    #adding neighbours of the node
    parent,child=map(int,raw_input().split())
    #directed graph
    alist[parent-1].append(child-1)
    

#topological sort function
stack=[]
visited=[0]*n
#select node,put in visited and explore children/neighbours
# to get same node number, increase value of node while adding in stack
def topological(node):
    visited[node]=True
    for item in alist[node]:
        if visited[item]==True:
            continue
        topological(item)
    stack.append(node)# increment value by one here to get original node number
    
for i in xrange(n):
    if visited[i]==False:
        topological(i)

print ' '.join(map(str,stack[::-1]))



# Print lexicographically smallest topological sort ordering
"""
n,edges=map(int,raw_input().split())
nodes=[i for i in xrange(n)]
alist=[[] for _ in xrange(n)]
#edges=input()
arr=[map(int,raw_input().split()) for i in xrange(edges)]
arr=sorted(arr)
for i in xrange(edges):
    #adding neighbours of the node
    parent,child=arr[i][0],arr[i][1]
    #directed graph
    alist[parent-1].append(child-1)
    

#topological sort function
stack=[]
visited=[0]*n
#select node,put in visited and explore children/neighbours
def topological(node):
    visited[node]=True
    for item in alist[node][::-1]:
        if visited[item]==True:
            continue
        topological(item)
    stack.append(node+1)
    
for i in xrange(n-1,0,-1):
    if visited[i]==False:
        topological(i)

print ' '.join(map(str,stack[::-1]))
"""




