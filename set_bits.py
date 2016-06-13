

""" COUNTS NUMBER OF 1s IN BINARY REPRESENTATION OF A NUMBER"""
""" ALGORITHM USED IS BRIAN KERNIGHAN ALGO"""
""" TIME COMPLEXITY IS Log(N)"""
def count_set_bits(n):
    count=0
    while n!=0:
        n &= n-1
        count=count+1
    return count
    
