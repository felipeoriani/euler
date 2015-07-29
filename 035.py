# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 035 - Circular primes
# How many circular primes are there below one million?
# ----------------------------------

# return an array of prime numbers using sieve of eratosthenes
def get_primes(n):
    r = []
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            r.append(i)
            multiples.update(range(i*i, n+1, i))
    return r

primes = get_primes(1000000)

def is_circular_prime(n):
    s = str(n)
    r = True
    for c in range(0, len(s)):
        s = s[1:] + s[0]
        if not int(s) in primes:
            r = False
            break
    return r    

def f(n):
    c = 0
    for i in primes:
        if is_circular_prime(i):
            print(i)
            c += 1
    return c

anwser = f(10**6)

assert anwser == 55

print('Answer: ', anwser)