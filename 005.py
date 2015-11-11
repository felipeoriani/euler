# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 005 - Smallest multiple
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# ----------------------------------

# greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# least common multiple
def lcm(a, b):
    return a / gcd(a, b) * b        

def f(minimum, maximum):
    internval = list(range(minimum, maximum+1))
    n = 1
    for i in range(minimum, maximum+1):
        n = lcm(n, i)
    return int(n)
        
anwser = f(1, 20)

assert anwser == 232792560

print 'Answer: ', anwser
