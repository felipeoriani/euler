# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 1 - Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below 1000.
# ----------------------------------

def f(n):
    sum = 0        
    for i in range(1, 1000):
        if i % n == 0:
            sum += i
    return sum

anwser = f(3) + f(5) - f(15)

print('Answer: ', anwser)

assert anwser == 233168