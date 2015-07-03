# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 002 - Even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# ----------------------------------

def fibonacci():
    a = b = 1
    while True:
        a, b = b, a+b        
        yield a

def f(n):
    term = s = 0
    fib = fibonacci()
    while term < n:
        # next term of fibonacci sequence
        term = next(fib)
        # sum only even terms
        if term % 2 == 0:
            s += term
    return s

anwser = f(10**6*4)

assert anwser == 4613732

print('Answer: ', anwser)