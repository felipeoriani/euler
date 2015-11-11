# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 014 - Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?
# ----------------------------------

memory = dict()

def seq(n):
    if n <= 1: 
        return 1
    if n in memory: 
        return memory.get(n)              
    r = seq(int(n / 2) if n % 2 == 0 else int(n * 3 + 1)) + 1    
    memory[n] = r
    return r

def f(n):
    s = 0
    m = 0
    for i in range(1, n):
        t = seq(i)
        if t > s:
            m = i
            s = t
    return m

anwser = f(10**6)

assert anwser == 837799

print 'Answer: ', anwser
