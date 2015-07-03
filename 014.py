# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 014 - Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?
# ----------------------------------

def collatz(n): 
    i = 0
    r = n
    while r > 1:
        if r % 2 == 0: 
            r = int(r / 2)
        else:
            r = int(r*3 + 1)
        i += 1
    return [i, n]

def f(n):
    m = 0
    maxStarting = 0
    for starting in range(0, n):
        c = collatz(starting) 
        if c > m:
            maxStarting = starting
            m = c
    return maxStarting

anwser = f(10**6)

#assert anwser == 233168

print('Answer: ', anwser)