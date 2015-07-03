# --------------------  --------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 010 - Summation of primes
# Find the sum of all the primes below two million.
# ----------------------------------
import math


def f(n, minimum, maximum):
    for a in range(minimum, maximum+1):
        for b in range(minimum, maximum+1):
            for c in range(minimum, maximum+1):
                m = (a**2) + (b**2) + (c**2)
                if math.log2(m) == n:
                    return (a) * (b) * (c)
    return 0

anwser = f(1000, 1, 1000)

#assert anwser == 142913828922

print('Answer: ', anwser)