# Segmented Sieve
# Mark primes in range [l,r]

l=10
r=20
prime=[True]*(r-l+1)
i=2
while i*i <= r:
    j=max(i*i, ((l+(i-1))/i) *i ) # Brackets added just for clarity
    # (l + (i - 1)) / i * i
    # this is the smallest integer greater or equal to "l" and divisible by "i"
    while j <= r:
        prime[j-l]=False
        j+=i
    i+=1

# Print whether the number is prime or not
for i,item in enumerate(prime,start=l):
	print i,item
