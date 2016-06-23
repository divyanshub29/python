# Adjacency List implementation
#Undirected graph
class Graph:
    def __init__(self):

        self.edges={}


    def addVertex(self,v):

        if v not in self.edges:
            self.edges[v]=[]


    def addEdge(self,from_v,to_v):

        if from_v not in self.edges:
            self.edges[from_v]
        if to_v not in self.edges:
            self.edges[to_v]=[]

        if to_v not in self.edges[from_v]:
            self.edges[from_v].append(to_v)
        if from_v not in self.edges(to_v):
            self.edges[to_v].append(from_v)

    def isEdge(self,from_v,to_v):
        #determines whether edge exists

        if to_v not in self.edges:
            return False
        if from_v not in self.edges:
            return False
        
        return to_v in self.edges[from_v]




simple = { 1:[2,3,5],
           2:[1,4],
           3:[1],
           4:[2,5],
           5:[1,4] }



def loadGraph(edges):
    '''Create a graph instance'''

    g=Graph()
    for v in edges:
        g.addVertex(v)
        for neighbor in edges[v]:
            g.addEdge(v,neighbor)

    return g





