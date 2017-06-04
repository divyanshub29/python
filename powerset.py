'''=== Powerset: All Subsets of a Set==='''
'''Make appropriate changes according to requirement, like if input data is
string instead of an array'''

arr=['a','b']
art=[]
fin=[]
count=0
l=len(arr)
ls=2**l
for i in range(ls):
    art=[]
    for j in range(l):
        if(i&(1<<j)):
            art.append(arr[j])
            print arr[j],
    print
    fin.append(art)
    print fin
