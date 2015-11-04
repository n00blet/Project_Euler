#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

from math import sqrt
import time
s=time.time()
def prime(num):
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(sqrt(num))+1):
        if num%i==0:
            return False
    return True


primes=[]
count=1

while len(primes) <=10000:
    count+=1
    if prime(count):
        primes.append(count)
print count
print time.time() - s
        
        


        
    
