def calculate_z(string):
    l=r=0   #l=left,r=right,k=iterator
    for k in xrange(1,total):
        if k > r:
            l = r = k
            while r < total and string[r] == string[r-l]:
                r+=1
            dp[k]= r-l
            r-=1
        else:
            k1=k-l
            if dp[k1] < r-k+1:
                dp[k] = dp[k1]
            else:
                l=k
                while r < total and string[r] == string[r-l]:
                    r+=1
                dp[k]= r-l
                r-=1

#input data and initializing variables
text=raw_input()
pat=raw_input()
total=len(text)+len(pat)+1
dp=[0]*total
string='$'.join([pat,text])

calculate_z(string)

#indices where a match occurs
for i in xrange(len(string)):
    if dp[i]==len(pat):
        print i-len(pat)-1
