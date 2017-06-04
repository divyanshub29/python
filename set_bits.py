

""" COUNTS NUMBER OF 1s IN BINARY REPRESENTATION OF A NUMBER"""
""" ALGORITHM USED IS BRIAN KERNIGHAN ALGO"""
""" TIME COMPLEXITY IS Log(N)in worst case,otherwise O(k) where k is number of set bits"""
def count_set_bits(n):
    count=0
    while n!=0:
        n &= n-1
        count=count+1
    return count
    

'''====check if the ith bit is set or not===='''

def checkbit(n,i):
    if(n&(1<<i)):
        return True
    return False


'''====generate all possible subset of a set==='''

def genSubsets(a):
    a=list(set(a))
    n=len(a)
    for i in range(2**n):
        for j in range(n):
            if i & (1<<j):
                print a[j],
        print ''

'''===largest power of 2 which is less than or equal to the given number N.==='''

def power2(n):
    n=n|(n>>1)
    n=n|(n>>2)
    n=n|(n>>4)
    n=n|(n>>8)

    return (n+1)>>1

