""" 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Follow this algo for faster solution --> https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
from math import sqrt
import time
s = time.time()

def sum_primes(limit):
    sieve = range(limit+1); sieve[1] = 0
    for n in xrange(2, int(sqrt(limit))+1):
        if sieve[n] > 0:
            for i in xrange(n*n, limit+1, n): sieve[i] = 0
    return sum(sieve)

print time.time() - s
print sum_primes(2000000)





