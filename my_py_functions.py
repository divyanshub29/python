def palindrome(a):
	length=len(a)
	iterator=0
	#original_length=length-1
	while iterator<length:
		if a[iterator]==a[length-iterator-1]:
			pass
		else:
			return False
		iterator=iterator+1
		if iterator==length:
			return True



def gcd(a, b):
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b) 
