# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 002 - 1000-digit Fibonacci number
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# ----------------------------------

def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a

def f(n):
    term = 0
    i = 1
    fib = fibonacci()
    while True:
        # next term of fibonacci sequence
        term = next(fib)
        if len(str(term)) == n:
            return i
        i += 1

anwser = f(1000)

assert anwser == 4782

print 'Answer: ', anwser
