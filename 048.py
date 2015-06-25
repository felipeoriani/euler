# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# Language.......: Python
# Problem 0048...: Self powers
# ----------------------------------

def f(n):
    s = 0
    for i in range(1, n+1):
        s += pow(i, i)
    return s

answer = f(1000) % 10000000000

assert answer == 9110846700

print('Answer: ', answer)