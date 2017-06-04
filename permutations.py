
def toString(List):
    #to return as string
    return ''.join(List)
    return List
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String,a
# 2. Starting index of the string,l
# 3. Ending index of the string.,r
def permute(a, l, r):
    if l==r:
        #return ''.join(a)
        print toString(a)
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            print "a before permute",
            print a
            permute(a, l+1, r)
            print "a after permute",
            print a
            a[l], a[i] = a[i], a[l] # backtrack
            print "after backtrack",
            print a

string = ['wlrbbmqbhcdarz', 'wk', 'yhiddqsc', 'xrjmowfrxsjybl', 'befsarc', 'ynecdyggx', 'p', 'lorellnmpapqfwk']
n = len(string)
a = string
permute(a, 0, n-1)

'''
# Python program to print all permutations with

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print ''.join(a)
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
 
# Driver program to test the above function
string = ['wlrbbmqbhcdarz', 'wk', 'yhiddqsc', 'xrjmowfrxsjybl', 'befsarc', 'ynecdyggx', 'p', 'lorellnmpapqfwk']
n = len(string)
a = string
permute(a, 0, n-1)
'''
