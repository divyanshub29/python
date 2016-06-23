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

