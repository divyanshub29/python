# Standard Question / Hackerearth Rectangle Sum Question
# Link --> https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/gold-mines-10/

# row and column
r,c=map(int,raw_input().split())
#array of array or matrix
arr=[map(int,raw_input().split()) for _ in xrange(r)]

#DP matrix
dp=[[0 for _ in xrange(c)] for i in xrange(r)]
dp[0][0]=arr[0][0]
for i in xrange(1,r):
    dp[i][0]=dp[i-1][0]+arr[i][0]

for i in xrange(1,c):
    dp[0][i]=dp[0][i-1]+arr[0][i]
for i in xrange(1,r):
    for j in xrange(1,c):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+arr[i][j]



# here loops runs for given number of queries
queries=input()
for query in xrange(queries):
    #Upper left and Lower right points of a rectangle
    x1,y1,x2,y2=map(int,raw_input().split())
    x1,y1,x2,y2=x1-1,y1-1,x2-1,y2-1
    x1,y1=x1-1,y1-1
    total=dp[x2][y2]
    flag=0
    if y1>=0:
        total=total-dp[x2][y1]
        flag+=1
    if x1>=0:
        total=total-dp[x1][y2]
        flag+=1
    if flag==2:
        total+=dp[x1][y1]
    print total #required answer
