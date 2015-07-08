# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 009 - Special Pythagorean triplet
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product a*b*c.
# ----------------------------------

def is_pythagorean_triplet(a, b, c):
    return (a**2)+(b**2)==(c**2) and a < b < c

def f(n):
    for a in range(3, n-3):
        for b in range(a+1, n-2):
            c = n-a-b            
            if is_pythagorean_triplet(a, b, c) and (a+b+c)==n:
                return a*b*c
    return 0

anwser = f(1000)

assert anwser == 31875000

print('Answer: ', anwser)