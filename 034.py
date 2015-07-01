# ----------------------------------
# Project Euler - projecteuler.net
# ----------------------------------
# Developed by Felipe B Oriani
# 34 - Digit factorials
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# ----------------------------------

def factorial(n): 
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def isCurious(n):
    s = 0
    for digit in map(int, str(n)):
        s += factorial(digit)
    return n == s

def f(max):
    s = 0
    for i in range(3, max+1):
        if isCurious(i):
            s += i
    return s

anwser = f(100000)

assert anwser == 40730

print('Answer: ', anwser)