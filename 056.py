# ---------------------------------- 
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 56 - Powerful digit sum
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum sum of each digit?
# ----------------------------------

def f(n):
    max = 0
    for base in range(1, n):
        for exp in range(1, n):
            r = pow(base, exp) 
            s = sum(map(int, str(base ** exp)))
            if (s > max): max = s
    return max

answer = f(100)

assert answer == 972

print('Anwser: ', answer)
