# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 010 - Summation of primes
# Find the sum of all the primes below two million.
# ----------------------------------

# return an array of prime numbers using sieve of eratosthenes
def primes(n):
    r = []
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            r.append(i)
            multiples.update(range(i*i, n+1, i))
    return r
 
def f(n):
    p = primes(n)
    return sum(p)

anwser = f(10**6*2)

assert anwser == 142913828922

print 'Answer: ', anwser
