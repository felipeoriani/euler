# ----------------------------------
# Project Euler - projecteuler.net
# ---------------------------------- 
# Developed by Felipe B Oriani
# 48 - Self powers
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000. 
# ----------------------------------

def f(n):
    s = 0
    for i in range(1, n+1):
        s += pow(i, i)
    return s

# use modular exponentiation principle
answer = f(1000) % 10000000000

assert answer == 9110846700

print('Answer: ', answer)