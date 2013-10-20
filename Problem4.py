# -*- coding: cp1252 -*-
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

"""
The palindrome can be written as:

    abccba

Which then simpifies to:

100000a + 10000b + 1000c + 100c + 10b + a

And then:

100001a + 10010b + 1100c

Factoring out 11, you get:

11(9091a + 910b + 100c)

So the palindrome must be divisible by 11.  Seeing as 11 is prime, at least one of the numbers must be divisible by 11.  So brute force in Python, only with less numbers to be checked:  """



def palin():
    maxx=maxI=maxJ=0
    i=999
    while(i>100):
        j=990
        while(j>100):
            product=i*j
            if product>maxx:
                y=str(product)
                if y==y[::-1]:
                    maxx=product
                    maxI=i
                    maxJ=j
            j-=11
        i-=1
    return maxx,maxI,maxJ
print palin()
        
    


       
