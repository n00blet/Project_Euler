#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from time import clock
def gcd(a,b):
    return b and gcd(b,a%b) or a
def lcm(a,b):
    return (a*b)/gcd(a,b)


count=20
for i in range(1,20):
    count=lcm(count,i)
print count


    
    
