# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 07 - 10001st prime
# What is the 10 001st prime number?
# ----------------------------------

def primes(n):
    if n <= 2:
        return []
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3)//2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom-top)//si)

    return [2]+filter(None, sieve)

for i in primes(10):
    print(i)

#assert answer == 25164150

#print('Answer: ', answer)
