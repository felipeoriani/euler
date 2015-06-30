# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 16 - Power digit sum
# What is the sum of the digits of the number 2^1000?
# ----------------------------------

def f(exp):
    s = 0
    r = 2 ** exp
    for digit in map(int, str(r)):
        s += digit
    return s

anwser = f(1000)

print('Answer: ', anwser)

#assert anwser == 1366