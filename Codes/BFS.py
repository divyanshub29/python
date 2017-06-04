'''===BFS===='''

adj=[[] for i in range(10)]
vis=[False]*10
level=[0 for i in range(10)]


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
    


