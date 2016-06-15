from time import time

def anagram(s1,s2):
        for key in s1:
                if key not in s2:
                        return False
        for item in s2:
                if item not in s1:
                        return False
        return True



def performance():
    now=time()

    for i in range(1,1000000):

        a='sdavbukasfjasbvdkhbasvhsabvikasgvvsajgsdjsdvjhsvhjvsdjsdvmjsdvsdjhsbxvssbjbsjvbbvsvjhsbvjhsbvjhsdbbsbvkusbvbsvgkuysgvjsbdvjvbsjhmsbysfugyufsgkyusfvkybvbhjl'
        b='sdavbukasfjasbvdkhbasvhsabvikasgvvsajgsdjsdvjhsvhjvsdjsdvmjsdvsdjhsbxvssbjbsjvbbvsvjhsbvjhsbvjhsdbbsbvkusbvbsvgkuysgvjsbdvjvbsjhmsbysfugyufsgkyusfvkybvbhjl'

        #'''code whose performance is to be evaluated'''
        anagram(a,b)

    done=time()


    print (done-now)*1000   #to clearly see the difference

performance()
