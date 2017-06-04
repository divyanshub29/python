
#size of board
n=input()

board=[[0 for _ in xrange(n)] for i in xrange(n)]

def  allowed(row,col,n):
    #checking for all columns upto i
    for i in xrange(col):
        if board[row][i]==1:
            return False

    #checking for upper left diagonal
    i,j=row,col
    while i>=0 and j>=0:
        if board[i][j]==1 :
            return False
        i,j=i-1,j-1

    #checking for lower left diagonal
    i,j=row,col
    while i<n and j>=0:
        if board[i][j]:
            return False
        i,j=i+1,j-1

    return True
    

def queen(col,n):
    
    #base condition
    if col>=n:
        return True

    #initiate recursion
    for i in xrange(n):
        if allowed(i,col,n):
            board[i][col]=1

            if queen(col+1,n):
                return True

        #bactracking condition
        board[i][col]=0
    return False



