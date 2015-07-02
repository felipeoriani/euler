# --------------------  --------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 007 - 10001st prime
# What is the 10001st prime number?
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
 
def f(max, index):
    p = primes(max)
    return p[index]

anwser = f(110000, 10000)

assert anwser == 104743

print('Answer: ', anwser)