# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 16 - Power digit sum
# What is the sum of the digits of the number 2^1000?
# ----------------------------------

def f(exp):    
    return sum(map(int, str(2 ** exp)))

anwser = f(1000)

print('Answer: ', anwser)

assert anwser == 1366