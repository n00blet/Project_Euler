""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. """

max_a,max_b,max_c=332,499,997
import time
s=time.time()
for a in range(1,max_a):
    for b in range(1,max_b):
        c=1000-a-b
        if c>b:
            if a**2+b**2==c**2:
                print a*b*c
                print a,b,c

print time.time()-s
            
