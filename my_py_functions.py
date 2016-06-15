'''======palindrome or not========'''
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

'''=======GCD of two numbers======'''

def gcd(a, b):
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b) 


'''========CONVERT INT TO A STRING IN ANY BASE==========='''

def toStr(number,base):
        convertString="0123456789ABCDEF" #for base 16, change for others
        if number<base:
                return convertString[number]
        else:
                return toStr(number//base,base) + convertString[number%base]



'''======ANAGRAM TESTER==========='''
def anagram(s1,s2):
        if len(s1)!=len(s2):
                return False
        for key in s1:
                if key not in s2:
                        return False
        for item in s2:
                if item not in s1:
                        return False
        return True


'''====ANAGRAM LEXICOGRAPHICALLY ARRANGED===='''
def anagramlex(s1,s2,value=0):
        #value:Lexicographically smallest or biggest
        #value: max=1 or min=0

        if anagram(s1,s2)==True:
                if value==0:
                        
                        s=''.join(sorted(s1))
                        return s
                
                else:
                        s=''.join(sorted(s1,reverse=True))
                        return s
                        
        else:
                return "Not an Anagram"


'''======check for pair in array with sum equal to some value======'''
def checkpair(arr,size,add):
        arr=sorted(arr)
        l=0
        r=size-1
        while l<r:
                if(arr[l]+arr[r]==add):
                        return 1
                elif (arr[l]+arr[r]<add):
                        l+=1
                else:
                        r-=1
        return 0




