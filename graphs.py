'''====GRAPHS===='''



'''===Adjacency Matrix==='''


#initializing the array
def initialize():
    arr=[[False]*10]*10
    print arr
    return arr


#Variables--> x,y,nodes,edges
arr=initialize()
nodes=input()
edges=input()

for i in range(edges):
    x,y=map(int,raw_input().split())
    #print x
    #print y
    arr[x][y]=True

if arr[3][4]==True:
    print "There is an edge between 3 and 4"

else:
    print "No edge is present between 3 and 4"


if arr[2][3]==True:
    print "there is an edge betwwen 2 and 3"
else:
    print" there is no edge betwwen 2 and 3"




'''===Adjacency List==='''


adj=[[] for x in range(10)]
print adj

nodes=input()
edges=input()

for i in range(edges):

    x,y=map(int,raw_input().split())
    adj[x].append(y)

print adj

#print adjacency of all list nodes

for i in range(1,nodes+1):
    print 'adjacency of %d' %i,
    for j in range(len(adj[i])):
        if j==len(adj[i])-1:
                  print adj[i][j]
        else:
                  print adj[i][j],
                  print '-->',


'''===DFS==='''
adj=[[] for i in range(10)]
visited=[False for j in range(10)]


def dfs(s):
    visited[s]=True
    for i in range(len(adj[s])):
        if visited[adj[s][i]]==False:
            dfs(adj[s][i])


def initialize():
    for i in range(10):
        visited[i]=False
    return





#main function
# Variables--> nodes,edges,x,,y,connectedComponents

connectedComponents=0

nodes=input()
edges=input()

for i in range(edges):
    x,y=map(int,raw_input().split())
    adj[x].append(y)
    adj[y].append(x)

initialize()

for i in range(1,nodes+1):
    if visited[i]==False:
        dfs(i)
        connectedComponents+=1


print "connectedComponets %d"% connectedComponents


'''===BFS===='''

adj=[[] for i in range(10)]
vis=[False]*10
level=[0 for i in range(10)]

# This implementation of Queue is inefficient, use in-built queue instead
class Queue:
    def __init__(self):
        self.items=[]


    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)


    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)





def bfs(s):
    q=Queue
    q.enqueue(s)
    level[s]=0
    vis[s]=True
    while (not q.isEmpty):
        p=q.items[-1]
        q.dequeue
        for i in range(len(adj[p])):
            if  vis[p][i]==False:
                level[v[p][i]]=level[p]+1
                q.enqueue(v[p][i])
                vis[v[p][i]]=True
    























































