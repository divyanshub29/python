def array(pattern):
    #length of pattern
    n=len(pattern)

    #making lsp array
    lsp=[0]*n

    index,i=0,1
    #loop to fill the array
    while i<n:
        #if characters match,then update value of lsp[i] with index+1
        if pattern[i]==pattern[index]:
            lsp[i]=index+1
            index+=1
            i+=1
        #else check for value at lsp[index-1] till a match is found or
        #index=0 is reached
        else:
            if index !=0:
                index=lsp[index-1]
            else:
                lsp[i]=0
                i+=1
    return lsp

def kmp(text,pattern):

    #making lsp array
    lsp=array(pattern)
    i=j=0
    #searching for pattern in text
    while i<len(text) and j<len(pattern):
        if text[i]==pattern[j]:
            i+=1
            j+=1
        else:
            #this part is executed in case suffix is same as prefix
            if j!=0:
                j=lsp[j-1]
            else:
                i+=1
        if j==len(pattern):
            return True
    else:
        return False
        
