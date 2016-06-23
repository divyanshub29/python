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

